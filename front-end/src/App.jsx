import Header from './components/Header';
import ResultBox from './components/ResultBox';
import Search from './components/Search';
import Footer from './components/Footer';
import './App.css'

function App() {

  return (
    <>
    <div>
      <Header />
    </div>
    <main>
      <Search />
      {/* <ResultBox />
      <ResultBox /> */}
    </main>
     <Footer/>
    </>
  )
}

export default App
