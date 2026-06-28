import AllUsers from './components/AllUsers';
import React, { useState, useEffect } from 'react';
import './App.css';
import Login from './components/Login';
import Signup from './components/Signup';
import AlgorithmSelector from './components/AlgorithmSelector';
import Visualizer from './components/Visualizer';
import Dashboard from './components/Dashboard';
import AlgorithmCode from './components/AlgorithmCode';

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [showLogin, setShowLogin] = useState(true);
  const [loading, setLoading] = useState(true);
  const [selectedAlgorithm, setSelectedAlgorithm] = useState('bubble-sort');

  useEffect(() => {
    // Check if user is already logged in
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
      setCurrentUser(JSON.parse(savedUser));
    }
    setLoading(false);
  }, []);

  useEffect(() => {
    // Listen for login/signup toggle events
    window.addEventListener('showLogin', () => setShowLogin(true));
    window.addEventListener('showSignup', () => setShowLogin(false));
    
    return () => {
      window.removeEventListener('showLogin', () => setShowLogin(true));
      window.removeEventListener('showSignup', () => setShowLogin(false));
    };
  }, []);

  const handleLoginSuccess = (user) => {
    setCurrentUser(user);
  };

  const handleSignupSuccess = (user) => {
    setCurrentUser(user);
  };

  const handleLogout = () => {
    localStorage.removeItem('user');
    setCurrentUser(null);
    setShowLogin(true);
  };

  const handleAlgorithmSelect = (algorithm) => {
    setSelectedAlgorithm(algorithm);
  };

  if (loading) {
    return <div style={{ padding: '20px' }}>Loading...</div>;
  }

  // If not logged in, show login/signup
  if (!currentUser) {
    return (
      <div>
        {showLogin ? (
          <Login onLoginSuccess={handleLoginSuccess} />
        ) : (
          <Signup onSignupSuccess={handleSignupSuccess} />
        )}
      </div>
    );
  }

  // If logged in, show algorithm visualizer
  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '20px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h1>Algorithm Visualizer</h1>
        <div>
          <span style={{ marginRight: '20px' }}>Welcome, {currentUser.username}!</span>
          <button onClick={handleLogout} style={{ padding: '8px 15px', backgroundColor: 'red', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
            Logout
          </button>
        </div>
      </div>
      
      <AlgorithmSelector onAlgorithmSelect={handleAlgorithmSelect} />
      <AlgorithmCode algorithm={selectedAlgorithm} />
      <Visualizer />
      <Dashboard />
      <AllUsers />
    </div>
  );
}

export default App;