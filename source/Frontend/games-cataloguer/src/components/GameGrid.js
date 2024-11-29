import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styling/GameGrid.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart as filledHeart } from '@fortawesome/free-solid-svg-icons';
import { faHeart as unfilledHeart } from '@fortawesome/free-regular-svg-icons';

const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:8000";

function GameGrid({ searchQuery }) {
  const [games, setGames] = useState([]); // Initialize as an empty array
  const [wishlist, setWishlist] = useState(new Set());
  const [currentPage, setCurrentPage] = useState(1);
  const [totalGames, setTotalGames] = useState(0);
  const PAGE_SIZE = 14;
  const [loading, setLoading] = useState(true);


  // Fetch games with pagination
  useEffect(() => {
    const skip = (currentPage - 1) * PAGE_SIZE;
    axios
      .get(`${apiUrl}/api/games?skip=${skip}&limit=${PAGE_SIZE}`)
      .then((response) => {
        setGames(response.data.games || []); // Default to an empty array
        setTotalGames(response.data.total || 0); // Default total to 0
        console.log(response.data.games);
      })
      .catch((error) => {
        console.error('Error fetching games:', error);
      })
      .finally(() => {
        setLoading(false); 
      });
  }, [currentPage]);

  // Fetch wishlist for the logged-in user
  useEffect(() => {
    const userId = localStorage.getItem('id');
    if (!userId) {
      console.log('No user logged in');
      return;
    }

    axios
      .get(`${apiUrl}/api/users/${userId}/wishlist`)
      .then((response) => {
        setWishlist(new Set(response.data.map((game) => game.id)));
      })
      .catch((error) => {
        console.error('Error fetching wishlist:', error);
      });
  }, []);

  // Add or remove game from wishlist
  const toggleWishlist = async (gameId) => {
    const userId = localStorage.getItem('id');
    if (!userId) {
      alert('You need to log in to manage your wishlist.');
      return;
    }

    try {
      if (wishlist.has(gameId)) {
        await axios.delete(`${apiUrl}/api/users/${userId}/wishlist/${gameId}`);
        setWishlist((prev) => {
          const updated = new Set(prev);
          updated.delete(gameId);
          return updated;
        });
      } else {
        await axios.post(`${apiUrl}/api/users/${userId}/wishlist/${gameId}`);
        setWishlist((prev) => new Set(prev).add(gameId));
      }
    } catch (error) {
      console.error('Error updating wishlist:', error);
      alert('Failed to update wishlist. Please try again.');
    }
  };

  // Filter games based on the search query
  const filteredGames = games.filter((game) =>
    game.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Handle pagination
  const totalPages = Math.ceil(totalGames / PAGE_SIZE);

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage((prev) => prev + 1);
    }
  };

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage((prev) => prev - 1);
    }
  };

  return (
    <>
      {loading ? (
        // render loading effect while waiting for the response
        <div className="loading-container">
          <p>Loading games...</p>
        </div>
      ) : (
        <>
          <div className="game-grid">
            {filteredGames.map((game) => (
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
                    onClick={() => toggleWishlist(game.id)}
                  >
                    <FontAwesomeIcon
                      icon={wishlist.has(game.id) ? filledHeart : unfilledHeart}
                    />
                  </button>
                </div>
              </div>
            ))}
          </div>
          <div className="pagination">
            <button onClick={handlePreviousPage} disabled={currentPage === 1}>
              Previous
            </button>
            <span>
              Page {currentPage} of {totalPages}
            </span>
            <button
              onClick={handleNextPage}
              disabled={currentPage === totalPages}
            >
              Next
            </button>
          </div>
        </>
      )}
    </>
  );
  
}

export default GameGrid;
