import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Header from './components/Header';
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
     
    </>
  )
}

export default App
