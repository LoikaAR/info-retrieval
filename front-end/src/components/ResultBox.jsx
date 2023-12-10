import React, { useState } from 'react';
import PropTypes from 'prop-types';
import HighlightedText from './HighlightedText';

const ResultBox = ({ name, region, category, distance, duration, ascent, description, link, query }) => {
  const [helpful, setHelpful] = useState(null);

  const handleCheckboxChange = (value) => {
    if (helpful === value) {
      // If the clicked checkbox is already selected, deselect it
      setHelpful(null);
    } else {
      setHelpful(value);
    }
  };

  return (
    <div className="result-box">
      {/* ... (existing content) ... */}
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
