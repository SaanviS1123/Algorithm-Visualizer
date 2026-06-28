import React, { useState, useEffect } from 'react';

function Dashboard() {
  const [metrics, setMetrics] = useState(null);
  const [algorithm, setAlgorithm] = useState(null);

  useEffect(() => {
    const handleAlgoSteps = (event) => {
      setMetrics(event.detail.metrics);
      const algo = localStorage.getItem('selectedAlgorithm');
      setAlgorithm(algo);
    };

    window.addEventListener('algo-steps', handleAlgoSteps);
    return () => window.removeEventListener('algo-steps', handleAlgoSteps);
  }, []);

  const complexityMap = {
    'bubble-sort': { time: 'O(n²)', space: 'O(1)' },
    'insertion-sort': { time: 'O(n²)', space: 'O(1)' },
    'quick-sort': { time: 'O(n log n)', space: 'O(log n)' },
    'merge-sort': { time: 'O(n log n)', space: 'O(n)' }
  };

  const complexity = algorithm ? complexityMap[algorithm] : null;

  if (!metrics) {
    return <div className="dashboard-container">Run an algorithm to see metrics...</div>;
  }

  return (
    <div className="dashboard-container">
      <h2>Algorithm Metrics</h2>

      <div className="metrics-grid">
        <div className="metric-card">
          <h3>Comparisons</h3>
          <p>{metrics.comparisons}</p>
        </div>

        <div className="metric-card">
          <h3>Swaps</h3>
          <p>{metrics.swaps}</p>
        </div>
      </div>

      <div className="complexity-info">
        <h3>Algorithm Complexity</h3>
        <p>Time Complexity: <strong>{complexity?.time || 'N/A'}</strong></p>
        <p>Space Complexity: <strong>{complexity?.space || 'N/A'}</strong></p>
      </div>
    </div>
  );
}

export default Dashboard;