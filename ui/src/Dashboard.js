import React from 'react';
import './styles.css';

const Dashboard = ({ handleLogout }) => {
    return (
        <div className="dashboard-container">
            <h2>Dashboard</h2>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Dashboard;