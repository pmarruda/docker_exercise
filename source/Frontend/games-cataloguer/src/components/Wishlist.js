import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styling/GameGrid.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart as filledHeart } from '@fortawesome/free-solid-svg-icons';

const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:8000";

function Wishlist() {
  const [wishlistGames, setWishlistGames] = useState([]); // Games in the wishlist
  const [loading, setLoading] = useState(true);

  // Fetch wishlist games for the logged-in user
  useEffect(() => {
    const userId = localStorage.getItem('id');
    if (!userId) {
      console.log('No user logged in');
      setLoading(false);
      return;
    }


    axios
      .get(`${apiUrl}/api/users/${userId}/wishlist`)
      .then((response) => {
        setWishlistGames(response.data || []);
        console.log(response.data);
      })
      .catch((error) => {
        console.error('Error fetching wishlist games:', error);
      })
      .finally(() => {
        setLoading(false); 
      });
  }, []);


  const removeFromWishlist = async (gameId) => {
    const userId = localStorage.getItem('id');
    if (!userId) {
      return;
    }

    try {
      await axios.delete(`${apiUrl}/api/users/${userId}/wishlist/${gameId}`);
      setWishlistGames((prev) => prev.filter((game) => game.id !== gameId));
    } catch (error) {
      console.error('Error removing game from wishlist:', error);
      alert('Failed to remove the game from your wishlist. Please try again.');
    }
  };

  return (
    <>
      {loading ? ( // Render loading effect while waiting for the response
        <div className="loading-container">
          <p>Loading your wishlist...</p>
        </div>
      ) : (
        <div className="game-grid">
          {wishlistGames.length > 0 ? (
            wishlistGames.map((game) => (
              <div key={game.id} className="game-card">
                <div className="game-image-container">
                  <img
                    src={`data:image/png;base64,${game.image}`}
                    alt={game.title}
                    className="game-image"
                  />
                </div>
                <div className="game-details">
                  <div className="game-text">
                    <h3 className="game-title">{game.title}</h3>
                    <p className="game-price">${game.price.toFixed(2)}</p>
                  </div>
                  <button
                    className="wishlist-button"
                    onClick={() => removeFromWishlist(game.id)}
                  >
                    <FontAwesomeIcon icon={filledHeart} />
                  </button>
                </div>
              </div>
            ))
          ) : (
            <p>No games in your wishlist yet.</p>
          )}
        </div>
      )}
    </>
  );
}

export default Wishlist;
