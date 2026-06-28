import React, { useState, useEffect } from 'react';

function AllUsers() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchAllUsers();
  }, []);

  const fetchAllUsers = async () => {
    try {
      const response = await fetch('http://localhost:5001/api/auth/all-users');
      const data = await response.json();
      setUsers(data.users);
      setLoading(false);
    } catch (err) {
      setError('Failed to load users');
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ padding: '20px' }}>Loading users...</div>;
  }

  if (error) {
    return <div style={{ padding: '20px', color: 'red' }}>{error}</div>;
  }

  return (
    <div style={{ padding: '20px', border: '1px solid #999', marginBottom: '20px', borderRadius: '5px' }}>
      <h2>All Registered Users ({users.length})</h2>

      {users.length === 0 ? (
        <p>No users registered yet.</p>
      ) : (
        <table style={{
          width: '100%',
          borderCollapse: 'collapse',
          marginTop: '20px'
        }}>
          <thead>
            <tr style={{ backgroundColor: '#f0f0f0', borderBottom: '2px solid #999' }}>
              <th style={{ padding: '10px', textAlign: 'left', borderRight: '1px solid #ddd' }}>ID</th>
              <th style={{ padding: '10px', textAlign: 'left', borderRight: '1px solid #ddd' }}>Username</th>
              <th style={{ padding: '10px', textAlign: 'left', borderRight: '1px solid #ddd' }}>Email</th>
              <th style={{ padding: '10px', textAlign: 'left' }}>Signup Date</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id} style={{ borderBottom: '1px solid #ddd' }}>
                <td style={{ padding: '10px', borderRight: '1px solid #ddd' }}>{user.id}</td>
                <td style={{ padding: '10px', borderRight: '1px solid #ddd' }}>{user.username}</td>
                <td style={{ padding: '10px', borderRight: '1px solid #ddd' }}>{user.email}</td>
                <td style={{ padding: '10px' }}>{user.created_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default AllUsers;