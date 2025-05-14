import React, { useState } from 'react';
import { addSleepData } from '../services/api';

const AddSleepData = ({ token, babyId }) => {
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [comments, setComments] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const sleepData = {
                startTime,
                endTime,
                comments,
                babyId,
            };
            await addSleepData(token, sleepData);
            alert('Sleep data added successfully');
        } catch (error) {
            alert('Failed to add sleep data');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="datetime-local" value={startTime} onChange={(e) => setStartTime(e.target.value)} />
            <input type="datetime-local" value={endTime} onChange={(e) => setEndTime(e.target.value)} />
            <textarea placeholder="Comments" value={comments} onChange={(e) => setComments(e.target.value)}></textarea>
            <button type="submit">Add Sleep Data</button>
        </form>
    );
};

export default AddSleepData;
