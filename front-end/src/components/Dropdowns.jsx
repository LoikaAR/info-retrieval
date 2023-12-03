import PropTypes from 'prop-types';
import Dropdown from './Dropdown';

const Dropdowns = ({ selectedOptions, handleOptionChange }) => {
  const handleOptionSelection = (index, option) => {
    handleOptionChange(index, option);
  };

  return (
    <div className="dropdowns">
      <Dropdown
        options={['Hiking', 'Biking', 'Adventure']}
        selectedOption={selectedOptions[0]}
        setSelectedOption={(option) => handleOptionSelection(0, option)}
      />
      <Dropdown
        options={['Hikin', 'Bikin', 'Adventur']}
        selectedOption={selectedOptions[1]}
        setSelectedOption={(option) => handleOptionSelection(1, option)}
      />
      <Dropdown
        options={['Hikings', 'Bikings', 'Adventures']}
        selectedOption={selectedOptions[2]}
        setSelectedOption={(option) => handleOptionSelection(2, option)}
      />
    </div>
  );
};

Dropdowns.propTypes = {
  selectedOptions: PropTypes.array.isRequired,
  handleOptionChange: PropTypes.func.isRequired,
};

export default Dropdowns;
