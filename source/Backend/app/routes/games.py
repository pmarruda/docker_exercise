from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..data import api_data
from .. import database

router = APIRouter(prefix="/games",  tags=["games"])

@router.get("/", response_model=list[api_data.Game])
def read_games(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return database.get_games(db, skip=skip, limit=limit)

@router.get("/{game_id}", response_model=api_data.Game)
def read_game(game_id: int, db: Session = Depends(database.get_db)):
    game = database.get_game(db, game_id=game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.post("/", response_model=api_data.Game)
def add_game(game: api_data.GameBase, db: Session = Depends(database.get_db)):
    return database.add_game(db, game)
