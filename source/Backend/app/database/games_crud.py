from sqlalchemy.orm import Session
from data.db_models import Game
from data.api_data import GameBase
import base64

def get_games(db: Session, skip: int = 0, limit: int = 10):
    total = db.query(Game).count()
    games = db.query(Game).order_by(Game.id.desc()).offset(skip).limit(limit).all()
    for game in games:
        game.image = base64.b64encode(game.image).decode("utf-8") if game.image else None
    return {"games": games, "total": total}

def get_game(db: Session, game_id: int):
    game = db.query(Game).filter(Game.id == game_id).first()
    if game and game.image:
        game.image = base64.b64encode(game.image).decode("utf-8")
    return game

def add_game(db: Session, game: GameBase):
    db_game = Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def remove_game(db: Session, game_id: int):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        return None
    db.delete(game)
    db.commit()
    return game.id
