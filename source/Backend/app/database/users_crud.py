from sqlalchemy.orm import Session
from data.db_models import User, Game
from data.api_data import UserCreate
from passlib.context import CryptContext
import base64

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password Utilities
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# User CRUD
def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

# Wishlist
def add_to_wishlist(db: Session, user_id: int, game_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        return None
    if game not in user.wishlist:
        user.wishlist.append(game)
        db.commit()
    return user

def remove_from_wishlist(db: Session, user_id: int, game_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        return None
    if game in user.wishlist:
        user.wishlist.remove(game)
        db.commit()
    return user

def get_user_wishlist(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    wishlist = user.wishlist.all()
    wishlist.reverse()
    for game in wishlist:
        game.image = base64.b64encode(game.image).decode("utf-8") if game.image else None
    return wishlist
