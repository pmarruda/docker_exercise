import React from 'react';
import '../styling/SearchBar.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCog } from '@fortawesome/free-solid-svg-icons';

function SearchBar({ setSearchQuery }) {
  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value); 
  };

  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search games..."
        onChange={handleSearchChange} 
      />
      <button className="filter-button">
        <FontAwesomeIcon icon={faCog} />
      </button>
    </div>
  );
}

export default SearchBar;
