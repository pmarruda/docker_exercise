from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from data import api_data

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=api_data.User)
def create_user(user: api_data.UserCreate, db: Session = Depends(database.get_db)):
    db_user = database.create_user(db, user)
    return db_user

@router.post("/login", response_model=api_data.UserBase)
def login(user: api_data.UserCreate, db: Session = Depends(database.get_db)):
    user = database.authenticate_user(db, user.username, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return {
        "id": user.id,
        "username": user.username,
    }

@router.get("/{user_id}", response_model=api_data.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = database.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/{user_id}/wishlist/{game_id}")
def add_to_wishlist(user_id: int, game_id: int, db: Session = Depends(database.get_db)):
    user = database.add_to_wishlist(db, user_id, game_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or Game not found")
    return {"message": f"Game {game_id} added to wishlist"}

@router.delete("/{user_id}/wishlist/{game_id}")
def remove_from_wishlist(user_id: int, game_id: int, db: Session = Depends(database.get_db)):
    user = database.remove_from_wishlist(db, user_id, game_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or Game not found")
    return {"message": f"Game {game_id} removed from wishlist"}

@router.get("/{user_id}/wishlist", response_model=list[api_data.Game])
def get_wishlist(user_id: int, db: Session = Depends(database.get_db)):
    wishlist = database.get_user_wishlist(db, user_id)
    if wishlist is None:
        raise HTTPException(status_code=404, detail="User not found")
    return wishlist

