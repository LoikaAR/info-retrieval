import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Dropdown from './Dropdown';
import { fetchRegionOptions, fetchCategoryOptions } from '../router.jsx';

const Dropdowns = ({ selectedOptions, handleOptionChange }) => {
  const [regionOptions, setRegionOptions] = useState([]);
  const [categoryOptions, setCategoryOptions] = useState([]);
  const [maxDistance, setMaxDistance] = useState(0.0);
  const [minDistance, setMinDistance] = useState(0.0);

  const handleOptionSelection = (field, option) => {
    handleOptionChange(field, option);
  };

  const handleMaxDistanceChange = (event) => {
    const value = parseFloat(event.target.value) || 0.0;
    setMaxDistance(value);
    handleOptionChange('distance', { ...selectedOptions.distance, max: value });
  };

  const handleMinDistanceChange = (event) => {
    const value = parseFloat(event.target.value) || 0.0;
    setMinDistance(value);
    handleOptionChange('distance', { ...selectedOptions.distance, min: value });
  };

  useEffect(() => {
    fetchRegionOptions(setRegionOptions);
    fetchCategoryOptions(setCategoryOptions);
  }, []);

  console.log("region options: " + regionOptions.regions);
  
  return (
    <div className="dropdowns">
      <span style={{ color: 'var(--primary)', margin: '10px' }}>Activities:</span>
      <span style={{ color: 'var(--primary)', margin: '10px' }}>Region:</span>
      <span style={{ color: 'var(--primary)', margin: '10px' }}>Distance:</span>
      <Dropdown
        options={categoryOptions.concat(['Any Category'])}
        selectedOption={selectedOptions.category}
        setSelectedOption={(option) => handleOptionSelection('category', option)}
      />
      <Dropdown
        options={regionOptions.concat(['Any Region'])}
        selectedOption={selectedOptions.region}
        setSelectedOption={(option) => handleOptionSelection('region', option)}
      />
      <div className='distance'>
        <input
          placeholder='Min:'
          type="text"
          value={minDistance === 0 ? '' : minDistance} // Display empty string if minDistance is 0
          onChange={handleMinDistanceChange}
        ></input>
        <input
          placeholder='Max:'
          type="text"
          value={maxDistance === 0 ? '' : maxDistance}
          onChange={handleMaxDistanceChange}
        ></input>
      </div>
    </div>
  );
};

Dropdowns.propTypes = {
  selectedOptions: PropTypes.shape({
    category: PropTypes.string.isRequired,
    region: PropTypes.string.isRequired,
    distance: PropTypes.shape({
      min: PropTypes.number.isRequired,
      max: PropTypes.number.isRequired,
    }).isRequired,
  }).isRequired,
  handleOptionChange: PropTypes.func.isRequired,
};

export default Dropdowns;
