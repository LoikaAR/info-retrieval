import { useState } from 'react'
import Header from './components/Header';
import ResultBox from './components/ResultBox';
import SearchBar from './components/SearchBar';
import Dropdown from './components/Dropdown';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div>
      <Header />
    </div>
    <main>
      <Dropdown />
      <SearchBar />
      <ResultBox />
    </main>
     
    </>
  )
}

export default App
