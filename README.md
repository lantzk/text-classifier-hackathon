# text-classifier-api

This project is a text classification API using FastAPI and a pre-trained sentiment analysis model, along with a Vue.js frontend.

## Docker Setup

1. Make sure you have Docker and Docker Compose installed on your system.

2. Build and run the Docker containers:

   ```
   docker-compose up --build
   ```

3. The API will be available at `http://localhost:8000`.

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

## Running the Full Stack

To run both the backend and frontend together:

1. Make sure you have Docker and Docker Compose installed.
2. From the project root directory, run:

   ```
   docker-compose up --build
   ```

3. The API will be available at `http://localhost:8000` and the frontend at `http://localhost:3000`.

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