import React, { useState } from 'react';
import axios from 'axios';

const registerUser = async (userData) => {
    try {
        const response = await axios.post('http://localhost:5000/api/auth/register', userData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log('Registration successful:', response.data);
    } catch (error) {
        console.error('Registration failed:', error);
        throw error;
    }
};

const Register = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await registerUser(formData);
            // handle successful registration (e.g., redirect or display message)
        } catch (error) {
            // handle registration error (e.g., display error message)
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email:</label>
                <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label>Password:</label>
                <input
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                />
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;
