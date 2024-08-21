# text-classifier-api

This project is a text classification API using FastAPI and a pre-trained sentiment analysis model, along with a Vue.js frontend.

## First-Time Setup

For first-time setup, we provide a convenient script that sets up both the backend and frontend:

1. Make sure you have Docker, Docker Compose, and Node.js installed on your system.

2. Run the setup script:

   ```
   chmod +x setup.sh
   ./setup.sh
   ```

   This script will:
   - Check for required dependencies
   - Build and start the Docker containers for the backend
   - Install frontend dependencies

3. After the script completes, the backend API will be available at `http://localhost:8000`.

4. To start the frontend development server, run:

   ```
   cd text-classifier-front-end && npm run dev
   ```

   The frontend will be available at `http://localhost:3000`.

## Manual Setup

If you prefer to set up the project manually, follow these steps:

### Docker Setup

1. Make sure you have Docker and Docker Compose installed on your system.

2. Build and run the Docker containers:

   ```
   docker-compose up --build
   ```

3. The API will be available at `http://localhost:8000`.

### Backend Setup (without Docker)

1. Navigate to the backend directory:

   ```
   cd text-classifier-api
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the backend using Uvicorn:

   ```
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

### Frontend Setup and Installation

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

## Running the Full Stack

To run both the backend and frontend together:

1. Make sure you have Docker and Docker Compose installed.
2. From the project root directory, run:

   ```
   docker-compose up --build
   ```

3. The API will be available at `http://localhost:8000` and the frontend at `http://localhost:3000`.

## API Documentation

You can access the FastAPI auto-generated documentation by visiting:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

These interactive documentation pages provide detailed information about all available endpoints, request/response models, and allow you to test the API directly from your browser.

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
  - PostgreSQL
  - Redis
  - SQLAlchemy
- Frontend:
  - Vue.js 3
  - Vuetify 3
  - TypeScript
  - Vite
- Deployment:
  - Docker
  - Docker Compose

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.