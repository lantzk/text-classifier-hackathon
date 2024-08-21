# text-classifier-api

This project is a text classification API using FastAPI and a pre-trained sentiment analysis model.

## Setup and Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/text-classifier-api.git
   cd text-classifier-api
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI app, use the following command:

```
uvicorn text_classifier_api.app:app --reload