import { useState, useEffect } from 'react';
import SearchBar from './SearchBar';
import Dropdowns from './Dropdowns';
import { getCSRFToken } from "../main.jsx";

function Search() {
  const [isVisible, setIsVisible] = useState(false);
  const [selectedOptions, setSelectedOptions] = useState({
    category: '',
    region: '',
    ascent: '',
  });

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
        ascent: '',
      });
    }
  }, [isVisible]);


  const handleFormSubmit = async (formData) => {
    try {
      const csrftoken = await getCSRFToken(); // Retrieve CSRF token

      if (csrftoken) {
        // Merge form data with selectedOptions object for submission
        const dataToSubmit = { ...formData, ...selectedOptions };

        // Send dataToSubmit to the backend
        const response = await fetch('http://127.0.0.1:8000/api/submit-form/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
          },
          body: JSON.stringify(dataToSubmit),
        });

        if (response.ok) {
          console.log('Form data submitted successfully');
          console.log("dataToSubmit: "+ JSON.stringify(dataToSubmit))
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

export default Search;
