import httpx
import os
from dotenv import load_dotenv
import logging
from pydantic import BaseModel
# from openai import OpenAI

from fastapi import HTTPException

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
LLM_URL = "https://api.openai.com/v1/chat/completions"

class TextInput(BaseModel):
    text: str

class ClassificationResult(BaseModel):
    factuality_score: float
    bias_score: float

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def classify_text(input_data: str) -> ClassificationResult:
    if not input_data:
        logger.warning("Empty text input received")
        raise HTTPException(status_code=400, detail="Please provide some text to classify.")
    
    logger.info(f"Classifying text: {input_data[:50]}...")  # Log first 50 characters

    prompt = f"""Analyze the following text related to Reproductive Justice and the proposed Amendment to the Ohio Constitution. Verify the information using credible sources such as Science Feedback, Health Feedback, FactCheck.org, Snopes, Guttmacher Institute, and VerifyThis. Avoid using non-credible sources, opinion pieces without factual backing, or sites with known bias that contradicts evidence-based standards.

Text to analyze: {input_data}

Provide your analysis in the following format:
1. TRUE or FALSE
2. Category (Misinformation, Disinformation, Malinformation, or Hate Speech)
3. Explanation (in a friendly, conversational tone)
4. Credible source reference
5. Recommended further reading

After your analysis, provide the following scores on separate lines:
Factuality score (0 = completely false, 1 = completely factual): [Your score here]
Bias score (0 = completely unbiased, 1 = extremely biased): [Your score here]

Ensure that the scores are provided as specified above, with each score on its own line."""

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                LLM_URL,
                headers={
                    "Authorization": f"Bearer {OPEN_AI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2
                },
                timeout=30.0  # Add a timeout
            )
        
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except httpx.RequestError as e:
        logger.error(f"Error making request to ChatGPT API: {str(e)}")
        raise HTTPException(status_code=500, detail="Error connecting to ChatGPT API")
    except httpx.HTTPStatusError as e:
        logger.error(f"ChatGPT API returned error status: {e.response.status_code}")
        raise HTTPException(status_code=500, detail=f"ChatGPT API error: {e.response.text}")

    try:
        result = response.json()
        content = result['choices'][0]['message']['content'].strip()
        
        logger.info(f"Raw API response content: {content}")  # Log the entire content
        
        # Split the content into lines
        lines = content.split('\n')
        
        # Initialize variables to store factuality and bias scores
        factuality_score = 0.5  # Default to neutral scores
        bias_score = 0.5
        
        # Look for the scores in the last lines of the content
        for line in reversed(lines):
            if 'Factuality score:' in line or 'Bias score:' in line:
                try:
                    score_parts = line.split(':')
                    if len(score_parts) >= 2:
                        score = float(score_parts[1].strip())
                        if 'Factuality score' in line:
                            factuality_score = score
                        elif 'Bias score' in line:
                            bias_score = score
                except ValueError as e:
                    logger.warning(f"Failed to parse score from: {line}. Error: {str(e)}")
        
        logger.info(f"Extracted scores - Factuality: {factuality_score}, Bias: {bias_score}")
        
        classification_result = ClassificationResult(
            factuality_score=factuality_score,
            bias_score=bias_score
        )
        
        logger.info(f"Classification complete. Factuality: {classification_result.factuality_score}, Bias: {classification_result.bias_score}")
        return classification_result
    except Exception as e:
        logger.error(f"Error processing API response: {str(e)}")
        # Return default scores if there's any error
        return ClassificationResult(factuality_score=0.5, bias_score=0.5)