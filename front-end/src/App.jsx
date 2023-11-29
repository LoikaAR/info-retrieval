import { useState } from 'react'
import Header from './components/Header';
import ResultBox from './components/ResultBox';
import Search from './components/Search';
import Footer from './components/Footer';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div>
      <Header />
    </div>
    <main>
      <Search />
      <ResultBox />
    </main>
     <Footer/>
    </>
  )
}

export default App
