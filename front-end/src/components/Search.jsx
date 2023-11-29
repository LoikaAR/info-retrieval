import SearchBar from './SearchBar';
import Dropdown from './Dropdown';

function Search() {

    return (
        <>
            <form className='search-container'>
                <SearchBar />
                <div className="dropdowns">
                    <Dropdown options={
                        ['Hiking', 'Biking', 'Adventure']
                    }/>
                </div>
            </form>
        </>
    )
}

export default Search
