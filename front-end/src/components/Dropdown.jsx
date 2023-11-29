
import { useState } from 'react';
import PropTypes from 'prop-types';

const Dropdown = ({options}) => {

  const [isOpen, setIsOpen] = useState(false);
  const [selectedoption, setSelectedoption] = useState('');

  const handleDropdownClick = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (option) => {
    setSelectedoption(option);
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
        {selectedoption || 'Select an option'}
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
            checked={selectedoption === option}
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
  };

export default Dropdown;


    //   <div className="dropdown" onClick={handleDropdownClick}>
    //     <span className="selected-option">{selectedoption || 'Select an option'}</span>
    //     <ul className={`options ${isOpen ? 'active' : ''}`}>
    //       {activities.map((option, index) => (
    //         <li key={index} onClick={() => handleOptionClick(option)}>
    //           {option}
    //         </li>
    //       ))}
    //     </ul>
    //   </div>

    // return (
    //     <>
    //         <div className="dropdown">
    //             <label htmlFor="activities">Choose Your option:</label>
    //             <div className="custom-select">
    //                 <span className="selected-option">Select an option</span>
    //                 <ul id="activities" className="options">
    //                     {activities.map((option, index) => (
    //                         <option key={index} value={option.toLowerCase()}>{option}</option>
    //                     ))}
    //                 </ul>
    //             </div>
    //         </div>
    //         <div className="dropdown">
    //             <label htmlFor="activities">Choose Your option:</label>
    //             <select name="activities" id="activities">
    //                 {activities.map((option, index) => (
    //                     <option key={index} value={option.toLowerCase()}>{option}</option>
    //                 ))}
    //             </select>
    //         </div>
    //     </>


    // );
    // return (
    //     <>
    //         {/* <div className="dropdown">
    //             <button className="dropbtn">Dropdown</button>
    //             <div className="dropdown-content">
    //                 <a href="#">Link 1</a>
    //                 <a href="#">Link 2</a>
    //                 <a href="#">Link 3</a>
    //             </div>
    //         </div> */}
    //         <form action="">
    //         <label for="options">Choose a option:</label>
    //         <select name="options" id="options">
    //             <option value="volvo">Volvo</option>
    //             <option value="saab">Saab</option>
    //             <option value="opel">Opel</option>
    //             <option value="audi">Audi</option>
    //         </select>
    //         <input type="submit" value="Submit"></input>
    //         </form>
    //     </>
    // );

