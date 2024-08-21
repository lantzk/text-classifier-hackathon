from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Set up the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Create FastAPI app
app = FastAPI(title="Text Classification API")

class TextInput(BaseModel):
    text: str

class ClassificationResult(BaseModel):
    label: str
    confidence: float

@app.post("/classify", response_model=ClassificationResult)
async def classify_text(input_data: TextInput):
    if not input_data.text:
        raise HTTPException(status_code=400, detail="Please provide some text to classify.")
    
    # Perform classification
    result = classifier(input_data.text)[0]
    
    return ClassificationResult(label=result['label'], confidence=result['score'])

@app.get("/")
async def root():
    return {"message": "Welcome to the Text Classification API"}

# Add some information about the API
@app.get("/about")
async def about():
    return {
        "info": "This is a simple text classification API using a pre-trained sentiment analysis model. You can replace it with your own text classification model for different tasks."
    }