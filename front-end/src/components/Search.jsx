import { useState, useEffect } from 'react';
import SearchBar from './SearchBar';
import Dropdowns from './Dropdowns';

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
      // Merge form data with selectedOptions object for submission
      const dataToSubmit = { ...formData, ...selectedOptions };

      // Send dataToSubmit to the backend
      const response = await fetch('http://127.0.0.1:8000/api/submit-form/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSubmit),
      });

      if (response.ok) {
        console.log('Form data submitted successfully');
        // Handle success response from the backend
      } else {
        console.error('Error submitting form data');
        // Handle error response from the backend
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
