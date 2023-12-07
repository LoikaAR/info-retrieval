import PropTypes from 'prop-types';

const HighlightedText = ({ text, query }) => {
  const queryWords = query.query.split(' ');
  const words = text.split(/\b/);

  return (
    <div className="result-description">
      {words.map((word, index) => {
        const isHighlighted = queryWords.includes(word.trim()); // Check trimmed word for highlighting

        return (
          <span key={index} style={{ backgroundColor: isHighlighted ? 'yellow' : 'transparent' }}>
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
