import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styling/GameGrid.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart } from '@fortawesome/free-solid-svg-icons';

function GameGrid() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/games')
      .then((response) => {
        setGames(response.data);
      })
      .catch((error) => {
        console.error('Error fetching games:', error);
      });
  }, []);

  const addToWishlist = async (gameId) => {
    const id = localStorage.getItem('id'); 

    if (!id) {
      alert('You need to log in to add games to your wishlist.');
      return;
    }

    try {
      await axios.post(`http://127.0.0.1:8000/api/users/${id}/wishlist/${gameId}`);
      alert('Game added to wishlist successfully!');
    } catch (error) {
      console.error('Error adding game to wishlist:', error);
      alert('Failed to add the game to your wishlist. Please try again.');
    }
  };

  return (
    <div className="game-grid">
      {games.map((game) => (
        <div key={game.id} className="game-card">
          <div className="game-image-container">
            <img src={game.image_url} alt={game.title} className="game-image" />
            <button
              className="wishlist-button"
              onClick={() => addToWishlist(game.id)} 
            >
              <FontAwesomeIcon icon={faHeart} />
            </button>
          </div>
          <div className="game-details">
            <h3 className="game-title">{game.title}</h3>
            <p className="game-price">${game.price.toFixed(2)}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default GameGrid;
