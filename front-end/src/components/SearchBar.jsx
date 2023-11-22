import React, { useState } from 'react';

const SearchBar = ({ handleSearch }) => {
  const [query, setQuery] = useState('');

  const handleChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    handleSearch(query);
    setQuery(''); // Resetting the query after search
  };

  return (
    <>
    
    <input
      className="search-input"
        type="text"
        placeholder="Search..."
        value={query}
        onChange={handleChange}
      />
      <button className="search-button" type="submit">Search</button>
    </>
  );
};

export default SearchBar;
