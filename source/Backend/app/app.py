from fastapi import FastAPI

from .data import db_models
from . import database
from .routes import games, users

# Initialize database
db_models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(games.router, prefix="/api")
app.include_router(users.router, prefix="/api")
