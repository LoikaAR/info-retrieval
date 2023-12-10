import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Dropdown from './Dropdown';
import { fetchRegionOptions, fetchCategoryOptions } from '../router.jsx';

const Dropdowns = ({ selectedOptions, handleOptionChange }) => {
  const [regionOptions, setRegionOptions] = useState([]);
  const [categoryOptions, setCategoryOptions] = useState([]);
  const [maxDistance, setMaxDistance] = useState('');
  const [minDistance, setMinDistance] = useState('');

  const handleOptionSelection = (field, option) => {
    handleOptionChange(field, option);
  };

  const handleMaxDistanceChange = (event) => {
    setMaxDistance(event.target.value);
    handleOptionChange('distance', { ...selectedOptions.distance, max: event.target.value });
  };

  const handleMinDistanceChange = (event) => {
    setMinDistance(event.target.value);
    handleOptionChange('distance', { ...selectedOptions.distance, min: event.target.value });
  };

  useEffect(() => {
    fetchRegionOptions(setRegionOptions);
    fetchCategoryOptions(setCategoryOptions);
  }, []);

  console.log("region options: " + regionOptions.regions);
  
  return (
    <div className="dropdowns">
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
        <span style={{ color: 'var(--primary)' }}>Distance:</span>
        <div style={{ display: 'flex', flexDirection: 'row' }}>
          <input
            placeholder='Max:'
            type="text"
            value={maxDistance}
            onChange={handleMaxDistanceChange}
          ></input>
          <input
            placeholder='Min:'
            type="text"
            value={minDistance}
            onChange={handleMinDistanceChange}
          ></input>
        </div>
      </div>
    </div>
  );
};

Dropdowns.propTypes = {
  selectedOptions: PropTypes.shape({
    category: PropTypes.string.isRequired,
    region: PropTypes.string.isRequired,
    distance: PropTypes.shape({
      min: PropTypes.string,
      max: PropTypes.string,
    }).isRequired,
  }).isRequired,
  handleOptionChange: PropTypes.func.isRequired,
};

export default Dropdowns;
