import PropTypes from 'prop-types';
import Dropdown from './Dropdown';

const Dropdowns = ({ selectedOptions, handleOptionChange }) => {
  const handleOptionSelection = (field, option) => {
    handleOptionChange(field, option);
  };

  return (
    <div className="dropdowns">
      <Dropdown
        options={['Hiking', 'Biking', 'Adventure', 'Any Activity']}
        selectedOption={selectedOptions.category}
        setSelectedOption={(option) => handleOptionSelection('category', option)}
      />
      <Dropdown
        options={['Ticino', 'Valais', 'Any Region']}
        selectedOption={selectedOptions.region}
        setSelectedOption={(option) => handleOptionSelection('region', option)}
      />
      {/* <Dropdown
        options={['Hikings', 'Bikings', 'Adventures',  'Any Activities']}
        selectedOption={selectedOptions.ascent}
        setSelectedOption={(option) => handleOptionSelection('ascent', option)}
      /> */}
    </div>
  );
};

Dropdowns.propTypes = {
  selectedOptions: PropTypes.shape({
    category: PropTypes.string.isRequired,
    region: PropTypes.string.isRequired,
    ascent: PropTypes.string.isRequired,
  }).isRequired,
  handleOptionChange: PropTypes.func.isRequired,
};

export default Dropdowns;
