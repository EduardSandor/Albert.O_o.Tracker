import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Login from '../pages/Login';
import Register from '../pages/Register';
import Prediction from '../pages/Prediction'; // Ensure correct import
import Navbar from '../components/Navbar';

const App = () => {
    return (
        <Router>
            <Navbar />
            <div className="App">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/prediction" element={<Prediction />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
