import { useState } from 'react'
import Header from './components/Header';
import ResultBox from './components/ResultBox';
import SearchBar from './components/SearchBar';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div>
      <Header />
    </div>
    <div className='main-content'>
      <SearchBar />
    </div>
    <div>
      <ResultBox />
    </div>
     
    </>
  )
}

export default App
