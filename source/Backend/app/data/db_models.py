from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table, LargeBinary
from sqlalchemy.orm import relationship
from database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    release_date = Column(Date)
    image = Column(LargeBinary)


#association table for wishlist
user_wishlist = Table(
    "user_wishlist",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("game_id", Integer, ForeignKey("games.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # hashed password
    wishlist = relationship("Game", secondary=user_wishlist, backref="wishlisted_games", lazy="dynamic")