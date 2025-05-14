import React, { useState } from 'react';
import axios from 'axios';
import '../pages/Prediction.css';

const Prediction = () => {
    const [ageInMonths, setAgeInMonths] = useState('');
    const [predictedData, setPredictedData] = useState(null);
    const [error, setError] = useState('');

    // Handle input changes
    const handleChange = (e) => {
        setAgeInMonths(e.target.value);
    };

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(''); // Reset error message

        try {
            // Make API request to get prediction
            const response = await axios.post('/api/predict_growth', { age_in_months: ageInMonths });
            setPredictedData(response.data);
        } catch (err) {
            console.error('Prediction API error:', err);
            setError('Prediction failed. Please try again.');
        }
    };

    return (
        <div>
            <h2>Predict Baby Growth</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Age in Months:</label>
                    <input
                        type="number"
                        value={ageInMonths}
                        onChange={handleChange}
                        required
                        min="0" // Ensures age is a non-negative number
                    />
                </div>
                <button type="submit">Predict</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {predictedData && (
                <div>
                    <h3>Predicted Data</h3>
                    <p>Height: {predictedData.predicted_height} cm</p>
                    <p>Weight: {predictedData.predicted_weight} kg</p>
                </div>
            )}
        </div>
    );
};

export default Prediction;
