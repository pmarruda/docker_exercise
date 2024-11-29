from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import users_crud
from database import get_db
from data import api_data

# Initialize the API router for users
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=api_data.User)
def create_user(user: api_data.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    Args:
        user (api_data.UserCreate): User creation details including username and password.
        db (Session): Database session dependency.

    Returns:
        api_data.User: The newly created user.
    """
    db_user = users_crud.create_user(db, user)
    return db_user

@router.post("/login", response_model=api_data.UserBase)
def login(user: api_data.UserCreate, db: Session = Depends(get_db)):
    """
    Authenticate a user with username and password.

    Args:
        user (api_data.UserCreate): Login credentials with username and password.
        db (Session): Database session dependency.

    Returns:
        api_data.UserBase: The authenticated user's ID and username.

    Raises:
        HTTPException: If the username or password is invalid.
    """
    user = users_crud.authenticate_user(db, user.username, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return {
        "id": user.id,
        "username": user.username,
    }

@router.get("/{user_id}", response_model=api_data.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve user details by user ID.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session): Database session dependency.

    Returns:
        api_data.User: The user's details including their wishlist.

    Raises:
        HTTPException: If the user with the given ID is not found.
    """
    user = users_crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/{user_id}/wishlist/{game_id}")
def add_to_wishlist(user_id: int, game_id: int, db: Session = Depends(get_db)):
    """
    Add a game to a user's wishlist.

    Args:
        user_id (int): The ID of the user.
        game_id (int): The ID of the game to add.
        db (Session): Database session dependency.

    Returns:
        dict: A success message.

    Raises:
        HTTPException: If the user or game is not found.
    """
    user = users_crud.add_to_wishlist(db, user_id, game_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or Game not found")
    return {"message": f"Game {game_id} added to wishlist"}

@router.delete("/{user_id}/wishlist/{game_id}")
def remove_from_wishlist(user_id: int, game_id: int, db: Session = Depends(get_db)):
    """
    Remove a game from a user's wishlist.

    Args:
        user_id (int): The ID of the user.
        game_id (int): The ID of the game to remove.
        db (Session): Database session dependency.

    Returns:
        dict: A success message.

    Raises:
        HTTPException: If the user or game is not found.
    """
    user = users_crud.remove_from_wishlist(db, user_id, game_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or Game not found")
    return {"message": f"Game {game_id} removed from wishlist"}

@router.get("/{user_id}/wishlist", response_model=list[api_data.Game])
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user's wishlist.

    Args:
        user_id (int): The ID of the user.
        db (Session): Database session dependency.

    Returns:
        list[api_data.Game]: A list of games in the user's wishlist.

    Raises:
        HTTPException: If the user is not found.
    """
    wishlist = users_crud.get_user_wishlist(db, user_id)
    if wishlist is None:
        raise HTTPException(status_code=404, detail="User not found")
    return wishlist
