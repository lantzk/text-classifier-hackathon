#!/bin/bash

# Exit on error
set -e

echo "Setting up text-classifier-api project..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js and try again."
    exit 1
fi

# Build and start Docker containers
echo "Building and starting Docker containers..."
docker-compose up --build -d

# Navigate to frontend directory
cd text-classifier-front-end

# Install frontend dependencies
echo "Installing frontend dependencies..."
npm install

echo "Setup complete!"
echo "Backend API is running at http://localhost:8000"
echo "To start the frontend development server, run:"
echo "cd text-classifier-front-end && npm run dev"
echo "The frontend will be available at http://localhost:3000"