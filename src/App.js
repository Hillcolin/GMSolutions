import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './Components/Home';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router> {/* Wrap the app in Router to enable routing */}
      <div className="App" id="background"> 

        {/* NavBar Portion */}
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <a className="navbar-brand" href="/">Roll Verse</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <a className="nav-link active" aria-current="page" href="/">Home</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        {/* Main Portion */}
        <div>
          
        </div>

      </div>
    </Router>
  );
}

export default App;
