import { useState } from 'react';
import Icon from '@mdi/react';
import { mdiMagnify } from '@mdi/js';

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
        placeholder="I want to go to..."
        value={query}
        onChange={handleChange}
      />
      <button className="search-button" type="submit">
        <Icon path={mdiMagnify} size={1} />
        </button>
    </>
  );
};

export default SearchBar;
