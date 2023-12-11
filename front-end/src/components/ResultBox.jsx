import { useState } from 'react';
import PropTypes from 'prop-types';
import HighlightedText from './HighlightedText';
import { getCSRFToken } from '../router';


const ResultBox = ({ name, region, category, distance, duration, ascent, description, link, query }) => {
  const [helpful, setHelpful] = useState(null);
  const submitRecommendation = async (nameValue, queryValue, setHelpfulValue) => {
    try {
      const csrftoken = await getCSRFToken();
  
      if (csrftoken) {
        const dataToSubmit = {
          name: nameValue,
          query: queryValue,
          setHelpful: setHelpfulValue,
        };
  
        const response = await fetch('http://localhost:8000/api/submit_recommendation/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify(dataToSubmit),
        });
  
        if (response.ok) {
          console.log('Recommendation submitted successfully');
          // Handle success response from the backend if needed
        } else {
          console.error('Error submitting recommendation');
          // Handle error response from the backend if needed
        }
      } else {
        console.log('Error: CSRF token retrieval failed');
        // Handle if CSRF token retrieval fails
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleCheckboxChange = (value) => {
      let newValue = value === helpful ? '' : value;
      setHelpful(newValue);
    
      submitRecommendation(name, query.query, newValue);
  };

  return (
    <div className="result-box">
      {console.log("the query iiiis: " + query.query)}
      {/* {setArr(highlightQuery())} */}
      <a className="result-link" href={link} target="_blank" rel="noreferrer">
        <h2 className="result-title">
          {name}
        </h2>
      </a>
      <div className="result-details">
        <h3 className="result-stats">
          Distance: {distance}
          <br />
          Duration: {duration}
          <br />
          Ascent: {ascent}
        </h3>
        <h3 className="result-category">
          Category: {category}
          <br />
          Region: {region}
        </h3>
      </div>
      {/* <p className="result-description">
        {description}
      </p> */}
      <HighlightedText text={description} query={query}/>
      
      {/* "Was This Helpful?" section */}
      <div className="helpful-section">
        <h3>Was This Helpful?</h3>
        <label>
          <input
            type="checkbox"
            value="Yes"
            checked={helpful === 'Yes'}
            onChange={() => handleCheckboxChange('Yes')}
          />
          Yes
        </label>
        <label>
          <input
            type="checkbox"
            value="No"
            checked={helpful === 'No'}
            onChange={() => handleCheckboxChange('No')}
          />
          No
        </label>
      </div>
    </div>
  );
};

ResultBox.propTypes = {
  name: PropTypes.string.isRequired,
  region: PropTypes.string.isRequired,
  category: PropTypes.string.isRequired,
  distance: PropTypes.string.isRequired,
  duration: PropTypes.string.isRequired,
  ascent: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  link: PropTypes.string.isRequired,
  query: PropTypes.object.isRequired,
};

export default ResultBox;
