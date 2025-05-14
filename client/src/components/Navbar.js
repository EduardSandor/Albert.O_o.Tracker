import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Optional: add CSS for styling

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/register">Register</Link></li>
                <li><Link to="/prediction">Prediction</Link></li>
                {/* Add more navigation links here */}
            </ul>
        </nav>
    );
};

export default Navbar;
