import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styling/Header.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';

function Header() {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  // Fetch the username from localStorage when the component mounts
  useEffect(() => {
    const storedUsername = localStorage.getItem('username');
    if (storedUsername) {
      setUsername(storedUsername);
    }
  }, []);

  // Logout functionality
  const handleLogout = () => {
    // Clear the cache
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('username');
    localStorage.removeItem('id');

    // Redirect to the login page
    navigate('/login');
  };

  return (
    <header className="header">
      <div className="logo">
        <span>GC</span>
        <a href="/" className="brand-name">
          Game Cataloguer
        </a>
      </div>
      <nav className="nav-links">
        <a href="/">Home</a>
        <a href="/wishlist">Wishlist</a>
        <a href="/recommendations">Recommendations</a>
        <a href="/comparison">Compare</a>
      </nav>
      <div className="profile">
        <button
          className="profile-icon"
          onClick={() => setDropdownOpen(!dropdownOpen)}
        >
          <FontAwesomeIcon icon={faUser} />
        </button>
        {dropdownOpen && (
          <div className="profile-dropdown">
            <p className="username-display">{username}</p>
            <hr />
            <a href="/wishlist">Wishlist</a>
            <hr />
            <button className="logout-button" onClick={handleLogout}>
              Logout
            </button>
          </div>
        )}
      </div>
    </header>
  );
}

export default Header;
