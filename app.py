from fastapi import FastAPI
from dotenv import load_dotenv
from text_classifier_api import TextInput, ClassificationResult, classify_text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Advanced Text Classification API")

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/text_classifier")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Redis setup
redis_client = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"))

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

# Add these lines at the end of the file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)