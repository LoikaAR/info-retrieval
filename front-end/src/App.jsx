import { useState, useEffect } from 'react';
import Header from './components/Header';
import ResultBox from './components/ResultBox';
import Search from './components/Search';
import Footer from './components/Footer';
import './App.css'
import { getCSRFToken } from "./main.jsx";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch CSRF token from Django server
        const csrftoken = await getCSRFToken();
        console.log("csrf token: "+csrftoken)
        // Fetch data from Django backend
        const response = await fetch('http://localhost:8000/api/get_data/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Include CSRF token in headers
          },
          credentials: 'include' // Send cookies along with the request
        });

        if (response.ok) {
          const jsonData = await response.json();
          setData(jsonData); // Set the received data to state
        } else {
          console.error('Failed to fetch data');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
    <div>
      <Header />
    </div>
    <main>
      <Search />
      {console.log("the object received from backend: " + data)}
      <div>
          {data.map((item, index) => (
            <ResultBox
              key={index}
              name={item.name}
              link={item.link}
              category={item.category}
              region={item.region}
              distance={item.distance}
              duration={item.duration}
              ascent={item.ascent}
              description={item.description.join('\n')}
            />
          ))}
        </div>
    </main>
     <Footer/>
    </>
  )
}

export default App
