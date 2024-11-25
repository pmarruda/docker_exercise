from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import Optional
from ..data import api_data
from datetime import date
from .. import database

router = APIRouter(prefix="/games",  tags=["games"])

@router.get("/", response_model=api_data.PaginatedGames)
def get_games(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return database.get_games(db, skip=skip, limit=limit)

@router.get("/{game_id}", response_model=api_data.Game)
def get_game(game_id: int, db: Session = Depends(database.get_db)):
    game = database.get_game(db, game_id=game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.delete("/{game_id}", response_model=int)
def delete_game(game_id: int, db: Session = Depends(database.get_db)):
    id = database.remove_game(db, game_id=game_id)
    if not id:
        raise HTTPException(status_code=404, detail="Game not found")
    return id

@router.post("/", response_model=int)
def add_game(
    title: str,
    description: Optional[str] = None,
    price: float = 0.0,
    release_date: Optional[date] = None,
    image: UploadFile = File(None),  # Optional file upload
    db: Session = Depends(database.get_db),
):
    # Read the image file as binary, if provided
    image_data = image.file.read() if image else None

    # Create a GameBase object to pass to the database method
    game_data = api_data.GameBase(
        title=title,
        description=description,
        price=price,
        release_date=release_date,
        image=image_data,
    )

    game = database.add_game(db, game_data)
    return game.id
