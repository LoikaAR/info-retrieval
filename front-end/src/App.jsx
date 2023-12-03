import { useState } from 'react';
import Header from './components/Header';
import ResultBox from './components/ResultBox';
import Search from './components/Search';
import Footer from './components/Footer';
import './App.css'
import { fetchData } from "./router.jsx";

function App() {
  const [data, setData] = useState([]);

  // useEffect(() => {
  //   fetchData(setData);
  // }, []);
  const handleSuccessfulPost = () => {
    // Function to handle successful post request triggering the get request
    fetchData(setData);
  };
  return (
    <>
    <div>
      <Header />
    </div>
    <main>
      <Search  onPostSuccess={handleSuccessfulPost}  />
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
    </main>
     <Footer/>
    </>
  )
}

export default App
