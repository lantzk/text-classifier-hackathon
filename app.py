from fastapi import FastAPI
from dotenv import load_dotenv
from text_classifier_api import TextInput, ClassificationResult, classify_text

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Advanced Text Classification API")

@app.post("/classify", response_model=ClassificationResult)
async def classify_text_endpoint(input_data: TextInput):
    return await classify_text(input_data)

@app.get("/")
async def root():
    return {"message": "Welcome to the Text Classification API"}

@app.get("/about")
async def about():
    return {
        "info": "This is an advanced text classification API using the Groq API to analyze text for factuality and bias."
    }