import Scroll from "./components/scroll";
import Upload from "./components/upload";
import Analysis from "./components/analysis";
import Visualization from "./components/visualization";
import "./styles/animations.css";

function App() {
  return (
    <>
      <nav className="navbar">
        <h1>Data Analyzer</h1>
      </nav>
      {/* HERO MESSAGE */}
      <div className="hero-message">
        <h2>Hello, let's analyse your dataset</h2>
        <p className="quote">
          "Without data, you're just another person with an opinion."
        </p>
      </div>

      <div className="main-container">

        <Scroll />

        <Upload />

        <Analysis />

        <Visualization />
       <footer className="footer">
          Built with React + FastAPI
        </footer>
      </div>

    </>
  );
}

export default App;