from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Advanced Text Classification API")

# Groq API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class TextInput(BaseModel):
    text: str

class ClassificationResult(BaseModel):
    factuality_score: float
    bias_score: float

@app.post("/classify", response_model=ClassificationResult)
async def classify_text(input_data: TextInput):
    if not input_data.text:
        raise HTTPException(status_code=400, detail="Please provide some text to classify.")
    
    # Prepare the prompt for Groq API
    prompt = f"""Analyze the following text and provide scores for factuality and bias on a scale of 0 to 1:

Text: {input_data.text}

Factuality score (0 = completely false, 1 = completely factual):
Bias score (0 = completely unbiased, 1 = extremely biased):

Provide only the scores as two float numbers separated by a comma, without any additional text."""

    # Call Groq API
    async with httpx.AsyncClient() as client:
        response = await client.post(
            GROQ_API_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mixtral-8x7b-32768",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2
            }
        )
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error calling Groq API")
    
    # Parse the response
    result = response.json()
    scores = result['choices'][0]['message']['content'].strip().split(',')
    
    return ClassificationResult(
        factuality_score=float(scores[0]),
        bias_score=float(scores[1])
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Text Classification API"}

@app.get("/about")
async def about():
    return {
        "info": "This is an advanced text classification API using the Groq API to analyze text for factuality and bias."
    }