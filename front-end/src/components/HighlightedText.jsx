import PropTypes from 'prop-types';
import { removeStopwords } from './RemoveStopwords';

const HighlightedText = ({ text, query }) => {
  function removePunctuation(word) {
    return word.replace(/[^\w]/g, '');
  }
  var queryWords = removeStopwords(query.query.toLowerCase()).split(/\s+/).filter(Boolean);
  
  const preprocessedWords = queryWords.map(function(word) {
    return removePunctuation(word)
  });
  
  const words = text.split(/\b/);

  return (
    <div className="result-description">
      {words.map((word, index) => {
        const isHighlighted = preprocessedWords.includes(word.trim().toLowerCase()) && word.trim().length > 0;
        return (
          <span key={index} style={{ backgroundColor: isHighlighted ? '#93cf72' : 'transparent', borderRadius:  '5px'}}>
            {word}
          </span>
        );
      })}
    </div>
  );
};

HighlightedText.propTypes = {
  text: PropTypes.string.isRequired,
  query: PropTypes.shape({
    query: PropTypes.string.isRequired
  }).isRequired
};

export default HighlightedText;
