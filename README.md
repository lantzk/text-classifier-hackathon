# text-classifier-api

This project is a text classification API using FastAPI and a pre-trained sentiment analysis model, along with a Vue.js frontend.

## Backend Setup and Installation

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

5. Create a `.env` file in the root directory and add your Groq API key:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Running the Backend Application

To run the FastAPI app, use the following command:

```
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`.

## Frontend Setup and Installation

1. Navigate to the frontend directory:

   ```
   cd text-classifier-front-end
   ```

2. Install the dependencies using your preferred package manager:

   ```
   npm install
   # or
   yarn install
   # or
   pnpm install
   ```

## Running the Frontend Application

To start the development server, run:

```
npm run dev
# or
yarn dev
# or
pnpm dev
```

The frontend will be available at `http://localhost:3000`.

## API Endpoints

- `GET /`: Welcome message
- `GET /about`: Information about the API
- `POST /classify`: Classify text for factuality and bias

## Technologies Used

- Backend:
  - FastAPI
  - Pydantic
  - httpx
  - Groq API
- Frontend:
  - Vue.js 3
  - Vuetify 3
  - TypeScript
  - Vite

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.