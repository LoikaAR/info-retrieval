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
      {/* TO DO: ensure to show result only if there is any query of length > 0 */}
      <ResultBox />
      <ResultBox />
    </main>
     <Footer/>
    </>
  )
}

export default App
