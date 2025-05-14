// services/api.js

import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // Adjust according to your backend URL

export const register = async (email, password) => {
    return axios.post(`${API_URL}/auth/register`, { email, password });
};

export const login = async (email, password) => {
    return axios.post(`${API_URL}/auth/login`, { email, password });
};

export const addSleepData = async (token, sleepData) => {
    return axios.post(`${API_URL}/sleep/add_sleep_data`, sleepData, {
        headers: { Authorization: `Bearer ${token}` }
    });
};

export const getSleepData = async (token, babyId) => {
    return axios.get(`${API_URL}/sleep/get_sleep_data`, {
        params: { babyId },
        headers: { Authorization: `Bearer ${token}` }
    });
};
