import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // Ensure to include this CSS

const Home = ({ token }) => {
    return (
        <div className="home-container">
            <div className="home-left">
                <h1>Welcome to OscarOGTracker</h1>
                <p>
                    Daddy's project made in order to track Albert Oscar's growth, making sure he's always on the right
                    path.
                    The scope is to use AI as much as possible to predict health issues and provide 100% clear
                    solutions.
                </p>
                <img src="/images/Eduard_Sandor_and_Albert_Sandor.JPG" alt="Albert Oscar" className="profile-picture"/>
            </div>
            <div className="vertical-separator"/>
            <div className="home-right">
                {!token ? (
                    <div className="auth-links">
                        <Link to="/login" className="auth-link">Login</Link>
                        <Link to="/register" className="auth-link">Register</Link>
                    </div>
                ) : (
                    <div className="dashboard">
                        {/* Place other components for authenticated users here */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Home;
