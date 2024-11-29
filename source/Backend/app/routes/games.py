from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import Optional
from data import api_data
from datetime import date
from database import games_crud
from database import get_db

# Initialize the API router for games
router = APIRouter(prefix="/games", tags=["games"])

@router.get("/", response_model=api_data.PaginatedGames)
def get_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a paginated list of games.

    Args:
        skip (int): Number of items to skip (for pagination). Default is 0.
        limit (int): Maximum number of items to retrieve. Default is 10.
        db (Session): Database session dependency.

    Returns:
        api_data.PaginatedGames: A paginated list of games and the total count.
    """
    return games_crud.get_games(db, skip=skip, limit=limit)

@router.get("/{game_id}", response_model=api_data.Game)
def get_game(game_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific game by its ID.

    Args:
        game_id (int): The ID of the game to retrieve.
        db (Session): Database session dependency.

    Returns:
        api_data.Game: The requested game's details.

    Raises:
        HTTPException: If the game with the given ID is not found.
    """
    game = games_crud.get_game(db, game_id=game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.delete("/{game_id}", response_model=int)
def delete_game(game_id: int, db: Session = Depends(get_db)):
    """
    Delete a game by its ID.

    Args:
        game_id (int): The ID of the game to delete.
        db (Session): Database session dependency.

    Returns:
        int: The ID of the deleted game.

    Raises:
        HTTPException: If the game with the given ID is not found.
    """
    id = games_crud.remove_game(db, game_id=game_id)
    if not id:
        raise HTTPException(status_code=404, detail="Game not found")
    return id

@router.post("/", response_model=int)
def add_game(
    title: str,
    description: Optional[str] = None,
    price: float = 0.0,
    release_date: Optional[date] = None,
    image: UploadFile = File(None),  # Optional file upload
    db: Session = Depends(get_db),
):
    """
    Add a new game to the database.

    Args:
        title (str): The title of the game. Required.
        description (Optional[str]): A brief description of the game. Optional.
        price (float): The price of the game. Default is 0.0.
        release_date (Optional[date]): The release date of the game. Optional.
        image (UploadFile): The game's image file (uploaded by the user). Optional.
        db (Session): Database session dependency.

    Returns:
        int: The ID of the newly created game.
    """
    # Read the image file as binary, if provided
    image_data = image.file.read() if image else None

    # Create a GameBase object to pass to the database method
    game_data = api_data.GameBase(
        title=title,
        description=description,
        price=price,
        release_date=release_date,
        image=image_data,
    )

    game = games_crud.add_game(db, game_data)
    return game.id
