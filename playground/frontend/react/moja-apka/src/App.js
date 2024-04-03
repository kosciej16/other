import logo from './logo.svg';
// import printMsg from "kosciej16-paczka";
import './App.css';

function App() {
  return (
    <div className="App">
    <div>
      <iframe width="1000" height="700" src="http://127.0.0.1:5000/v1/link/link/?jwt=eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJyZWRpcmVjdF91cmkiOiJodHRwOi8vMTI3LjAuMC4xIiwiZXhwIjozNDY3MjAyNzIzLjAzNDIzNn0.ntNJAWZCee4Zf6A-PlD3g55LeadVhHD7NmNbGKBVW6-tsx0mK0zPbHOnHxZ-hXwgk4oh9mQYBbQHUVHIW7PfCQ
" title="description"></iframe>
      <button id="mojeid">MAIN</button>

    </div>
    <div>
      <iframe width="1000" height="700" src="http://127.0.0.1:5000/v1/link/link/tmp" title="ABC"></iframe>
    </div>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
