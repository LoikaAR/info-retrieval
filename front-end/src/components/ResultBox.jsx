import { useState } from 'react';
import PropTypes from 'prop-types';
import HighlightedText from './HighlightedText';
// import fs from 'fs';


const ResultBox = ({ name, region, category, distance, duration, ascent, description, link, query }) => {
  const [helpful, setHelpful] = useState(null);
  
  const handleCheckboxChange = (value) => {
    if (helpful === value) {
      // If the clicked checkbox is already selected, deselect it
      setHelpful(null);
    } else {
      setHelpful(value);
    }
    console.log(name)

    fetch('../../public/ordered_json_file.json').then(response => {
      return response.json();
    }).then(data => {
      for (let i = 0; i < data.length; i++) {
        if (data[i].name === name) {
          console.log(data[i].docno)
          break
        }
      }
      // TODO - frontend
      // post request containing docno and yes/no option
      
      // todo - backend
      // receive post request 
        // subtract the score of the item if used fedback 'no' and store it in the feedback.json (together with query)
        // add to the score if the feedbcak is 'yes'
      // console.log(docno)
    })
    .catch(error => console.error('Error fetching the JSON file:', error));

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
