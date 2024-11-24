from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
from .data import api_data
from .data import db_models
import os
from dotenv import load_dotenv

load_dotenv()

#Database URL
DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

#SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#GAMES
def get_games(db: Session, skip: int = 0, limit: int = 10):
    return db.query(db_models.Game).offset(skip).limit(limit).all()

def get_game(db: Session, game_id: int):
    return db.query(db_models.Game).filter(db_models.Game.id == game_id).first()

def add_game(db: Session, game: api_data.GameBase):
    db_game = db_models.Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

#USERS
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: api_data.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = db_models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(db_models.User).filter(db_models.User.id == user_id).first()

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(db_models.User).filter(db_models.User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def add_to_wishlist(db: Session, user_id: int, game_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    game = db.query(db_models.Game).filter(db_models.Game.id == game_id).first()
    if not game:
        return None
    if not user.wishlist.filter(db_models.Game.id == game_id).first():
        user.wishlist.append(game)
        db.commit()
    return user

def remove_from_wishlist(db: Session, user_id: int, game_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    game = db.query(db_models.Game).filter(db_models.Game.id == game_id).first()
    if not game:
        return None
    if user.wishlist.filter(db_models.Game.id == game_id).first():
        user.wishlist.remove(game)
        db.commit()
    return user

def get_user_wishlist(db: Session, user_id: int):
    user = db.query(db_models.User).filter(db_models.User.id == user_id).first()
    if not user:
        return None
    return user.wishlist.all()