from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# GAMES
class GameBase(BaseModel):
    """
    Represents the base structure for a game.

    Attributes:
        title (str): The title of the game.
        description (Optional[str]): A brief description of the game. Optional.
        price (float): The price of the game.
        release_date (Optional[date]): The release date of the game. Optional.
        image (Optional[bytes]): The game's image in bytes. Optional.
    """
    title: str
    description: Optional[str]
    price: float
    release_date: Optional[date]
    image: Optional[bytes]

class Game(GameBase):
    """
    Represents a game with an ID for database interactions.

    Attributes:
        id (int): The unique identifier for the game.
    """
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models.

class PaginatedGames(BaseModel):
    """
    Represents a paginated response for games.

    Attributes:
        games (List[Game]): A list of games in the current page.
        total (int): The total number of games available.
    """
    games: List[Game]
    total: int

# USER
class UserBase(BaseModel):
    """
    Represents the base structure for a user.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
    """
    id: int
    username: str

class UserCreate(BaseModel):
    """
    Represents the structure for creating a new user.

    Attributes:
        username (str): The desired username for the new user.
        password (str): The password for the new user.
    """
    username: str
    password: str

class User(UserBase):
    """
    Represents a user with additional attributes.

    Attributes:
        id (int): The unique identifier for the user.
        wishlist (List[Game]): A list of games the user has added to their wishlist.
    """
    id: int
    wishlist: List[Game] = []  # Default to an empty list for the wishlist.

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models.
