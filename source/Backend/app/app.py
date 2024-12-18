from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import db_models
from database import engine
from routes import games, users
import os
from dotenv import load_dotenv
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator

# Load environment variables from .env file
load_dotenv()

# Initialize the FastAPI application
app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:80", "http://games-frontend:80", "http://127.0.0.1"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Include routers for API endpoints
app.include_router(games.router, prefix="/api")
app.include_router(users.router, prefix="/api")

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)

# Initialize database schema (only when run as the main script)
if __name__ == "__main__":
    db_models.Base.metadata.create_all(bind=engine)
    
    # Get port from environment variable APP_PORT, default to 8000 if not set
    app_port = int(os.getenv("APP_PORT", "8000"))

    # Run the FastAPI application using Uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=app_port
    )
