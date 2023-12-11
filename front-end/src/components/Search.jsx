import { useState, useEffect } from 'react';
import SearchBar from './SearchBar';
import Dropdowns from './Dropdowns';
import { getCSRFToken } from "../router.jsx";
import PropTypes from 'prop-types';

function Search({ onPostSuccess, setSearchOptions }) {
  const [isVisible, setIsVisible] = useState(false);
  const [selectedOptions, setSelectedOptions] = useState({
    category: '',
    region: '',
    distance: { min: 0.0, max: 0.0 },
  });

  useEffect(() => {
    setSearchOptions(selectedOptions);
  }, [selectedOptions, setSearchOptions]);

  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };

  const handleOptionChange = (field, value) => {
    setSelectedOptions({
      ...selectedOptions,
      [field]: value,
    });
  };

  useEffect(() => {
    // Reset selectedOptions if the dropdowns were visible but now hidden
    if (!isVisible) {
      setSelectedOptions({
        category: '',
        region: '',
        distance: { min: 0.0, max: 0.0 },
      });
    }
  }, [isVisible]);


  const handleFormSubmit = async (formData) => {
    try {
      const csrftoken = await getCSRFToken();

      if (csrftoken) {
        // Merge form data with selectedOptions object for submission (for filtering purposes in the back-end)
        // formData.query = formData.query.replace(/[^\w]/g, '');
        const dataToSubmit = { ...formData, ...selectedOptions };

        const response = await fetch('http://127.0.0.1:8000/api/submit-form/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify(dataToSubmit),
        });

        if (response.ok) {
          console.log('Form data submitted successfully');
          console.log("dataToSubmit: "+ JSON.stringify(dataToSubmit))
          onPostSuccess(formData); // Trigger the function in App component to execute the GET request
          // Handle success response from the backend
        } else {
          console.error('Error submitting form data');
          // Handle error response from the backend
        }
      } else {
        console.log('Error: CSRF token retrieval failed');
        // Handle if CSRF token retrieval fails
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <>
      <div className='search-container'>
        <SearchBar handleFormSubmit={handleFormSubmit} />
        <button type="button" onClick={toggleVisibility} className="show-dropdowns">
          {isVisible ? 'Hide Categories' : 'Show me all Categories!'}
        </button>
        {isVisible && (
          <Dropdowns selectedOptions={selectedOptions} handleOptionChange={handleOptionChange} />
        )}
        {console.log("selectedOptions object: ", selectedOptions)}
      </div>
    </>
  );
}

Search.propTypes = {
  onPostSuccess: PropTypes.func.isRequired,
  setSearchOptions: PropTypes.func.isRequired,
};

export default Search;
