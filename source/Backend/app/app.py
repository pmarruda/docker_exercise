from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .data import db_models
from . import database
from .routes import games, users

db_models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(games.router, prefix="/api")
app.include_router(users.router, prefix="/api")
