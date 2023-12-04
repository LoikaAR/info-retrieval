import { useState } from 'react';
import Icon from '@mdi/react';
import { mdiMagnify } from '@mdi/js';
import PropTypes from 'prop-types';

const SearchBar = ({ handleFormSubmit }) => {
  const [query, setQuery] = useState('');

  const handleChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    handleFormSubmit({ query }); // pass query to the parent component for submission
    // setQuery(''); // reset query after submission
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <input
        className="search-input"
        type="text"
        placeholder="I want to go to..."
        value={query}
        onChange={handleChange}
        autoFocus
      />
      <button className="search-button" type="submit">
        <Icon path={mdiMagnify} size={1} />
      </button>
    </form>
  );
};

SearchBar.propTypes = {
  handleFormSubmit: PropTypes.func.isRequired,
};

export default SearchBar;
