import { useState } from 'react';
import SearchBar from './SearchBar';
import Dropdowns from './Dropdowns';

function Search() {
  const [isVisible, setIsVisible] = useState(false);
  const [selectedOptions, setSelectedOptions] = useState(['', '', '']);

  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };

  const handleOptionChange = (index, option) => {
    const newSelectedOptions = [...selectedOptions];
    newSelectedOptions[index] = option;
    setSelectedOptions(newSelectedOptions);
  };

  return (
    <>
      <form className='search-container'>
        <SearchBar />
        <button type="button" onClick={toggleVisibility} className="show-dropdowns">
          {isVisible ? 'Hide Categories' : 'Show me all Categories!'}
        </button>
        {isVisible && (
          <Dropdowns selectedOptions={selectedOptions} handleOptionChange={handleOptionChange} />
        )}
        {console.log("selectedOptions array: " + selectedOptions)}
      </form>
    </>
  );
}

export default Search;
