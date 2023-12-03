import { useState } from 'react';
import PropTypes from 'prop-types';

const Dropdown = ({ options, selectedOption, setSelectedOption }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleDropdownClick = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (option) => {
    if (option.includes("Any")) {
      option = "";
    }
    setSelectedOption(option);
    setIsOpen(false);
  };
  

  return (
    <div className={`custom-select ${isOpen ? 'active' : ''}`}>
      <button
        type="button"
        className="select-button"
        onClick={handleDropdownClick}
        aria-haspopup="listbox"
        aria-expanded={isOpen}
      >
        <span className="selected-value">
          {selectedOption || 'Select an option'}
          {/* we can use selectedOption in the query for finding the relevant results */}
          {/* {console.log("selectedOption length: " + selectedOption.length)}
          {console.log("selected Option: " + selectedOption)} */}
        </span>
        <span className="arrow"></span>
      </button>
      <ul className="select-dropdown">
        {options.map((option, index) => (
          <li key={index} onClick={() => handleOptionClick(option)}>
            <input
              type="radio"
              id={option}
              name="options"
              checked={selectedOption === option}
              readOnly
            />
            <label htmlFor={option}>{option}</label>
          </li>
        ))}
      </ul>
    </div>
  );
};

Dropdown.propTypes = {
  options: PropTypes.arrayOf(PropTypes.string).isRequired,
  selectedOption: PropTypes.string.isRequired,
  setSelectedOption: PropTypes.func.isRequired,
};

export default Dropdown;