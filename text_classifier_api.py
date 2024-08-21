import httpx
import os
from dotenv import load_dotenv
import logging
from pydantic import BaseModel
from fastapi import HTTPException
import re
from typing import List, Dict

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
LLM_URL = "https://api.openai.com/v1/chat/completions"

class Claim(BaseModel):
    truth_value: str
    category: str
    explanation: str
    source: str

class ClassificationResult(BaseModel):
    factuality_score: float
    bias_score: float
    claims: List[Claim]
    further_reading: List[Dict[str, str]]

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
                timeout=30.0
            )
        
        response.raise_for_status()
    except httpx.RequestError as e:
        logger.error(f"Error making request to ChatGPT API: {str(e)}")
        raise HTTPException(status_code=500, detail="Error connecting to ChatGPT API")
    except httpx.HTTPStatusError as e:
        logger.error(f"ChatGPT API returned error status: {e.response.status_code}")
        raise HTTPException(status_code=500, detail=f"ChatGPT API error: {e.response.text}")

    try:
        result = response.json()
        content = result['choices'][0]['message']['content'].strip()
        
        logger.info(f"Raw API response content: {content}")
        
        # Extract scores
        factuality_score = float(re.search(r'Factuality score.*?:\s*([\d.]+)', content, re.IGNORECASE).group(1))
        bias_score = float(re.search(r'Bias score.*?:\s*([\d.]+)', content, re.IGNORECASE).group(1))
        
        # Process claims
        claims = process_claims(content)
        
        # Extract further reading
        further_reading = extract_further_reading(content)
        
        classification_result = ClassificationResult(
            factuality_score=factuality_score,
            bias_score=bias_score,
            claims=claims,
            further_reading=further_reading
        )
        
        logger.info(f"Classification complete. Factuality: {classification_result.factuality_score}, Bias: {classification_result.bias_score}")
        return classification_result
    except Exception as e:
        logger.error(f"Error processing API response: {str(e)}")
        return ClassificationResult(
            factuality_score=0.5, 
            bias_score=0.5, 
            claims=[],
            further_reading=[]
        )

def process_claims(content: str) -> List[Claim]:
    claims = []
    claim_pattern = re.compile(r'(\d+)\.\s*(TRUE|FALSE)\s*\n(\d+)\.\s*Category:\s*(.*?)\s*\n(\d+)\.\s*Explanation:\s*(.*?)\s*\n(\d+)\.\s*Credible source reference:\s*(.*?)\s*\n', re.DOTALL)
    
    for match in claim_pattern.finditer(content):
        claims.append(Claim(
            truth_value=match.group(2),
            category=match.group(4),
            explanation=match.group(6).strip(),
            source=match.group(8)
        ))
    
    return claims

def extract_further_reading(content: str) -> List[Dict[str, str]]:
    further_reading = []
    for match in re.finditer(r'Recommended further reading:\s*\[([^\]]+)\]\(([^)]+)\)', content):
        further_reading.append({
            "title": match.group(1),
            "url": match.group(2)
        })
    return further_reading