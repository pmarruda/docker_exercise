# Backend for Game Cataloguer

This is the backend application for the Game Cataloguer, built with FastAPI and PostgreSQL.

## Prerequisites

- Python 3.10 or higher
- PostgreSQL

## Installation

1. Navigate to the backend directory:

   ```bash
   cd source/Backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file with the contents from [.docker/envs/backend.env](../../.docker/envs/backend.env) 
## Running the Application

1. Start the FastAPI server:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:8000/docs` to access the API documentation.

## Database Initialization

1. Initialize the database with the provided SQL script:

   ```bash
   psql -U user -d games_database -f scripts/init_db.sql
   ```

## Docker

1. Build the Docker image:

   ```bash
   docker build -t games-backend -f .docker/Dockerfile.backend .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 games-backend
   ```