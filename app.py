from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from text_classifier_api import TextInput, ClassificationResult, classify_text
from typing import Annotated
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Advanced Text Classification API")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/classify", response_class=HTMLResponse)
async def classify_text_endpoint(request: Request, claim: Annotated[str, Form()]):
    result = await classify_text(claim)
    return templates.TemplateResponse("result.html", {"request": request, "result": result, "claim": claim})

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
async def about():
    return {
        "info": "This is an advanced text classification API using the Groq API to analyze text for factuality and bias."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)