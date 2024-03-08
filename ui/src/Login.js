import React, { useState } from 'react';
import './styles.css'; // Import CSS file

const Login = ({ handleLogin, error }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        handleLogin(username, password);
    };

    return (
        <div className="login-container">
            <div className="login-left">
                <h2>Login</h2>
                <form className="login-form" onSubmit={handleSubmit}>
                    <div className="input-group">
                        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                    </div>
                    <div className="input-group">
                        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    </div>
                    <button className="button" type="submit">Login</button>
                    {error && <div className="error">{error}</div>}
                </form>
            </div>
            <div className="login-right"></div>
        </div>
    );
};

export default Login;