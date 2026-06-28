import React, { useState } from 'react';

function AlgorithmSelector({ onAlgorithmSelect }) {
  const [algorithm, setAlgorithm] = useState('bubble-sort');
  const [datasetSize, setDatasetSize] = useState(20);
  const [loading, setLoading] = useState(false);

  const generateDataset = () => {
    return Array.from({ length: datasetSize }, () => Math.floor(Math.random() * 100));
  };

  const handleAlgorithmChange = (e) => {
    const newAlgorithm = e.target.value;
    setAlgorithm(newAlgorithm);
    onAlgorithmSelect(newAlgorithm);
  };

  const handleRunAlgorithm = async () => {
    setLoading(true);
    const dataset = generateDataset();

    try {
      const response = await fetch('http://localhost:5001/api/run-algorithm', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          algorithm: algorithm,
          dataset: dataset
        })
      });

      const data = await response.json();

      localStorage.setItem('selectedAlgorithm', algorithm);

      window.dispatchEvent(
        new CustomEvent('algo-steps', {
          detail: {
            ...data,
            algorithm: algorithm
          }
        })
      );
    } catch (error) {
      console.error('Error:', error);
      alert('Error running algorithm!');
    }

    setLoading(false);
  };

  return (
    <div className="selector-container">
      <h2>Algorithm Selector</h2>

      <label>
        Algorithm:
        <select 
          value={algorithm} 
          onChange={handleAlgorithmChange}
        >
          <option value="bubble-sort">Bubble Sort</option>
          <option value="quick-sort">Quick Sort</option>
          <option value="merge-sort">Merge Sort</option>
          <option value="insertion-sort">Insertion Sort</option>
        </select>
      </label>

      <label style={{ marginLeft: '30px' }}>
        Dataset Size:
        <input
          type="number"
          value={datasetSize}
          onChange={(e) => setDatasetSize(Number(e.target.value))}
          min="5"
          max="100"
        />
      </label>

      <br />

      <button 
        className="run-btn"
        onClick={handleRunAlgorithm} 
        disabled={loading}
      >
        {loading ? 'Running...' : 'Run Algorithm'}
      </button>
    </div>
  );
}

export default AlgorithmSelector;