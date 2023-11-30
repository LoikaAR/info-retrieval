import { useState } from 'react';
import SearchBar from './SearchBar';
import Dropdown from './Dropdown';

function Search() {

    const [isVisible, setIsVisible] = useState(false);
    const [selectedOption, setSelectedOption] = useState('');

    const toggleVisibility = () => {
        setIsVisible(!isVisible);
        if (!isVisible) {
            setSelectedOption("Hide Categories");
        } else {
            setSelectedOption("Show me all Categories!")
        }
    };

    return (
        <>
            <form className='search-container'>
                <SearchBar />
                <button type="button" onClick={toggleVisibility} className="show-dropdowns">{selectedOption || 'Show me all Categories!'}</button>
                {isVisible && (
                    <div className="dropdowns">
                        {/* MULTIPLE DROPDOWN-SELECTS CHANGE EACH OTHER'S VALUES ATM, EXTREMELY NOT SECURE */}
                        <Dropdown options={
                            ['Hiking', 'Biking', 'Adventure']
                        } />
                        <Dropdown options={
                            ['Hiking', 'Biking', 'Adventure']
                        } />
                        <Dropdown options={
                            ['Hiking', 'Biking', 'Adventure']
                        } />
                    </div>
                )}

            </form>
        </>
    )
}

export default Search
