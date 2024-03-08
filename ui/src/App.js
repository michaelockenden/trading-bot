import React, { useState } from 'react';
import Login from './Login';
import Dashboard from './Dashboard';

const App = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [error, setError] = useState('');

    const handleLogin = async (username, password) => {
        try {
            if (username.trim() !== '') {
                setIsLoggedIn(true);
                setError('');
            } else {
                throw new Error('Invalid username or password');
            }
        } catch (error) {
            setError('Invalid username or password');
        }
    };

    const handleLogout = () => {
        setIsLoggedIn(false);
    };

    return (
        <div className="App">
            {isLoggedIn ? (
                <Dashboard handleLogout={handleLogout} />
            ) : (
                <Login handleLogin={handleLogin} error={error} />
            )}
        </div>
    );
};

export default App;