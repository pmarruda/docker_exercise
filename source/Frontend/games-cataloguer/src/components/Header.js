import React, { useState } from 'react';
import '../styling/Header.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser} from '@fortawesome/free-solid-svg-icons';

function Header() {
  const [dropdownOpen, setDropdownOpen] = useState(false);

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
        <a href="#recommended">Recommended</a>
        <a href="#comparison">Comparison</a>
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
            <a href="#linked-accounts">Linked Accounts</a>
            <hr />
            <a href="#played-games">Played Games</a>
            <hr />
            <a href="#wish-list">Wishlist</a>
            <hr />
            <a href="#settings">Settings</a>
          </div>
        )}
      </div>
    </header>
  );
}

export default Header;
