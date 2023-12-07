import PropTypes from 'prop-types';
import HighlightedText from './HighlightedText';

const ResultBox = ({ name, region, category, distance, duration, ascent, description, link, query }) => {
 
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
