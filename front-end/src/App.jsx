import { useState } from 'react';
import Header from './components/Header';
import ResultBox from './components/ResultBox';
import Search from './components/Search';
import Footer from './components/Footer';
import './App.css';
import { fetchData } from './router.jsx';

function App() {
  const [data, setData] = useState([]);
  const [query, setQuery] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [resultsPerPage] = useState(5); // Number of results to display per page
  const maxButtonsToShow = 10; // Maximum number of page buttons to display

  const handleSuccessfulPost = (query) => {
    // Function to handle successful post request triggering the get request
    fetchData(setData);
    setQuery(query);
    setCurrentPage(1); // Reset to first page when new data is fetched
  };

  // Logic to calculate pagination
  const indexOfLastResult = currentPage * resultsPerPage;
  const indexOfFirstResult = indexOfLastResult - resultsPerPage;
  const currentResults = data.slice(indexOfFirstResult, indexOfLastResult);

  // Function to change page
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  const renderPaginationButtons = () => {
    const buttons = [];
    let startPage;
    let endPage;
    const totalPages = Math.ceil(data.length / resultsPerPage);

    if (totalPages <= maxButtonsToShow) {
      startPage = 1;
      endPage = totalPages;
    } else {
      if (currentPage <= Math.ceil(maxButtonsToShow / 2)) {
        startPage = 1;
        endPage = maxButtonsToShow;
      } else if (currentPage + Math.floor(maxButtonsToShow / 2) >= totalPages) {
        startPage = totalPages - maxButtonsToShow + 1;
        endPage = totalPages;
      } else {
        startPage = currentPage - Math.floor(maxButtonsToShow / 2);
        endPage = currentPage + Math.floor(maxButtonsToShow / 2);
      }
    }
    
    const goToBeginning = () => {
      paginate(1);
    };

    const goToEnd = () => {
      paginate(totalPages);
    };

    // Rendering "Go to Beginning" button
    if (startPage !== 1) {
      buttons.push(
        <li key="goToBeginning">
          <button onClick={goToBeginning}>Go to Beginning</button>
        </li>
      );
    }

    for (let i = startPage; i <= endPage; i++) {
      buttons.push(
        <li key={i}>
          <button onClick={() => paginate(i)}>{i}</button>
        </li>
      );
    }

    // Rendering "Go to End" button
    if (endPage !== totalPages) {
      buttons.push(
        <li key="goToEnd">
          <button onClick={goToEnd}>Go to End</button>
        </li>
      );
    }

    return buttons;
  };

  return (
    <>
      <div>
        <Header />
      </div>
      <main>
        <Search onPostSuccess={handleSuccessfulPost} />
        {currentResults.map((item, index) => (
          <ResultBox
            key={index}
            name={item.name}
            link={item.link}
            category={item.category}
            region={item.region}
            distance={item.distance}
            duration={item.duration}
            ascent={item.ascent}
            description={item.description}
            query={query}
          />
        ))}
        {/* Pagination */}
        <div>
          {data.length > resultsPerPage && (
            <ul className="pagination">
              {renderPaginationButtons()}
            </ul>
          )}
        </div>
      </main>
      <Footer />
    </>
  );
}

export default App;
