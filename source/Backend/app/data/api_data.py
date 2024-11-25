from pydantic import BaseModel
from typing import List, Optional
from datetime import date

#GAMES
class GameBase(BaseModel):
    title: str
    description: Optional[str]
    price: float
    release_date: Optional[date]
    image: Optional[bytes]

class Game(GameBase):
    id: int

    class Config:
        orm_mode = True

class PaginatedGames(BaseModel):
    games: List[Game]
    total: int

#USER
class UserBase(BaseModel):
    id: int
    username: str

class UserCreate(BaseModel):
    username: str
    password: str 

class User(UserBase):
    id: int
    wishlist: List[Game] = [] 

    class Config:
        orm_mode = True