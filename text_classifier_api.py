import httpx
import os
from pydantic import BaseModel
from fastapi import HTTPException

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class TextInput(BaseModel):
    text: str

class ClassificationResult(BaseModel):
    factuality_score: float
    bias_score: float

async def classify_text(input_data: TextInput) -> ClassificationResult:
    if not input_data.text:
        raise HTTPException(status_code=400, detail="Please provide some text to classify.")
    
    prompt = f"""Analyze the following text and provide scores for factuality and bias on a scale of 0 to 1:

Text: {input_data.text}

Factuality score (0 = completely false, 1 = completely factual):
Bias score (0 = completely unbiased, 1 = extremely biased):

Provide only the scores as two float numbers separated by a comma, without any additional text."""

    async with httpx.AsyncClient() as client:
        response = await client.post(
            GROQ_API_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2
            }
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error calling Groq API")
    
    result = response.json()
    scores = result['choices'][0]['message']['content'].strip().split(',')
    
    return ClassificationResult(
        factuality_score=float(scores[0]),
        bias_score=float(scores[1])
    )