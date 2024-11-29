from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table, LargeBinary
from sqlalchemy.orm import relationship
from database import Base

class Game(Base):
    """
    Represents a game in the database.

    Attributes:
        id (int): The unique identifier for the game.
        title (str): The title of the game. This field is required.
        description (str): A brief description of the game. Optional.
        price (float): The price of the game. This field is required.
        release_date (date): The release date of the game. Optional.
        image (bytes): The game's image in binary format. Optional.
    """
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    release_date = Column(Date)
    image = Column(LargeBinary)


# Association table for the many-to-many relationship between users and their wishlisted games
user_wishlist = Table(
    "user_wishlist",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("game_id", Integer, ForeignKey("games.id"), primary_key=True),
)


class User(Base):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user. This field is unique and required.
        password (str): The hashed password of the user. This field is required.
        wishlist (List[Game]): A list of games the user has added to their wishlist.
            This is implemented as a many-to-many relationship with the Game model.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # hashed password
    wishlist = relationship(
        "Game", 
        secondary=user_wishlist,  # Uses the association table to define the relationship
        backref="wishlisted_games",  # Creates a reverse reference from Game to User
        lazy="dynamic"  # Enables efficient querying for large relationships
    )
