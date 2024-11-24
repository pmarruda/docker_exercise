from pydantic import BaseModel
from typing import List, Optional
from datetime import date

#GAMES
class GameBase(BaseModel):
    title: str
    description: Optional[str]
    price: float
    release_date: Optional[date]
    image_url: Optional[str]

class Game(GameBase):
    id: int

    class Config:
        orm_mode = True

#USER
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str 

class User(UserBase):
    id: int
    wishlist: List[Game] = [] 

    class Config:
        orm_mode = True