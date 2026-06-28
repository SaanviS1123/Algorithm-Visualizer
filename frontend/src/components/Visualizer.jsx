import React, { useState, useEffect } from 'react';

function Visualizer() {
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [autoPlay, setAutoPlay] = useState(false);

  useEffect(() => {
    const handleAlgoSteps = (event) => {
      setSteps(event.detail.steps);
      setCurrentStep(0);
      setAutoPlay(false);
    };

    window.addEventListener('algo-steps', handleAlgoSteps);
    return () => window.removeEventListener('algo-steps', handleAlgoSteps);
  }, []);

  useEffect(() => {
    if (!autoPlay || steps.length === 0) return;

    const interval = setInterval(() => {
      setCurrentStep((prev) => {
        if (prev >= steps.length - 1) {
          setAutoPlay(false);
          return prev;
        }
        return prev + 1;
      });
    }, 50);

    return () => clearInterval(interval);
  }, [autoPlay, steps]);

  if (steps.length === 0) {
    return <div className="visualizer-container">Run an algorithm first...</div>;
  }

  const currentData = steps[currentStep];

  return (
    <div className="visualizer-container">
      <h2>Visualization</h2>

      <div className="bar-chart">
      {currentData.array.map((value, index) => (
          <div
            key={index}
            className={`bar ${currentData.comparing.includes(index) ? 'comparing' : 'default'}`}
            style={{ height: `${value * 2}px` }}
          >
            <span className="bar-value">{value}</span>
          </div>
        ))}
      </div>

      <div className="compare-info">
        {currentData.comparing.length > 0 ? (
          <p>
            <strong>Comparing:</strong> {currentData.array[currentData.comparing[0]]} 
            {' ↔ '}
            {currentData.array[currentData.comparing[1]]}
          </p>
        ) : (
          <p>No comparisons</p>
        )}
      </div>

      <div className="controls">
        <button onClick={() => setCurrentStep(Math.max(0, currentStep - 1))}>Previous</button>
        <span className="step-info">Step {currentStep + 1} / {steps.length}</span>
        <button onClick={() => setCurrentStep(Math.min(steps.length - 1, currentStep + 1))}>Next</button>
        <button onClick={() => setAutoPlay(!autoPlay)}>
          {autoPlay ? 'Pause' : 'Play'}
        </button>
      </div>
    </div>
  );
}

export default Visualizer;