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
    const sanitizedQuery = query.replace(/[^\w\s]/gi, ''); // Remove special characters
    if (sanitizedQuery.trim() !== query.trim()) {
      showNotification('Please avoid using special characters.'); // Display browser notification
      return; // Prevent form submission
    }
    handleFormSubmit({ query: sanitizedQuery.trim() }); // Pass sanitized query to the parent component for submission
    // setQuery(''); // Reset query after submission
  };

  const showNotification = (message) => {
    if (Notification.permission === 'granted') {
      new Notification('Error', {
        body: message,
      });
    } else if (Notification.permission !== 'denied') {
      Notification.requestPermission().then((permission) => {
        if (permission === 'granted') {
          new Notification('Error', {
            body: message,
          });
        }
      });
    }
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
