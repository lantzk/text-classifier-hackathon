import httpx
import os
import logging
from pydantic import BaseModel
# from openai import OpenAI

from fastapi import HTTPException

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

async def classify_text(input_data: TextInput) -> ClassificationResult:
    if not input_data.text:
        logger.warning("Empty text input received")
        raise HTTPException(status_code=400, detail="Please provide some text to classify.")
    
    logger.info(f"Classifying text: {input_data.text[:50]}...")  # Log first 50 characters

    prompt = f"""Analyze the following text and provide scores for factuality and bias on a scale of 0 to 1:

Text: {input_data.text}

Factuality score (0 = completely false, 1 = completely factual):
Bias score (0 = completely unbiased, 1 = extremely biased):

Provide only the scores as two float numbers separated by a comma, without any additional text."""

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
        scores = result['choices'][0]['message']['content'].strip().split(',')
        
        if len(scores) != 2:
            raise ValueError("Unexpected number of scores returned")
        
        classification_result = ClassificationResult(
            factuality_score=float(scores[0]),
            bias_score=float(scores[1])
        )
        logger.info(f"Classification complete. Factuality: {classification_result.factuality_score}, Bias: {classification_result.bias_score}")
        return classification_result
    except (KeyError, IndexError, ValueError) as e:
        logger.error(f"Error parsing ChatGPT API response: {str(e)}")
        raise HTTPException(status_code=500, detail="Error parsing ChatGPT API response")