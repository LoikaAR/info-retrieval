import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Dropdown from './Dropdown';
import { fetchRegionOptions, fetchCategoryOptions } from '../router.jsx';

const Dropdowns = ({ selectedOptions, handleOptionChange }) => {
  const [regionOptions, setRegionOptions] = useState([]);
  const [categoryOptions, setCategoryOptions] = useState([]);

  const handleOptionSelection = (field, option) => {
    handleOptionChange(field, option);
  };
  
  useEffect(() => {
    fetchRegionOptions(setRegionOptions); 
    fetchCategoryOptions(setCategoryOptions); 
  }, []);

   // Empty dependency array ensures this effect runs only once after initial render
  console.log("region options: "+regionOptions.regions)
  return (
    <div className="dropdowns">
      <Dropdown
        options={categoryOptions.concat(['Any Category'])}
        selectedOption={selectedOptions.category}
        setSelectedOption={(option) => handleOptionSelection('category', option)}
      />
      <Dropdown
        options={regionOptions.concat(['Any Region'])} // Combine fetched options with 'Any Region'
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
    distance: PropTypes.string.isRequired,
  }).isRequired,
  handleOptionChange: PropTypes.func.isRequired,
};

export default Dropdowns;
