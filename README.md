# Algorithm Visualizer

An interactive web application for visualizing sorting algorithms in real time. The platform allows users to create accounts, explore algorithm behavior through animations, and analyze performance metrics such as comparisons, swaps, and execution time.

## Features

### Authentication

* User Signup
* User Login
* Secure user management

### Sorting Algorithm Visualizations

* Bubble Sort
* Insertion Sort
* Merge Sort
* Quick Sort

### Real-Time Visualization

* Step-by-step algorithm animations
* Dynamic array generation
* Adjustable visualization controls

### Performance Metrics Dashboard

* Number of comparisons
* Number of swaps
* Execution time analysis
* Algorithm performance comparison

## Tech Stack

### Frontend

* React
* JavaScript
* HTML/CSS

### Backend

* Python
* Flask

### Database

* SQLite

## Project Structure

```text
Algorithm-Visualizer/
│
├── backend/
│   ├── src/
│   │   ├── algorithms/
│   │   ├── models/
│   │   ├── auth.py
│   │   └── server.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/SaanviS1123/Algorithm-Visualizer.git
cd Algorithm-Visualizer
```

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend
npm install
```

## Running the Application

### Start Backend

```bash
cd backend
python src/server.py
```

### Start Frontend

```bash
cd frontend
npm start
```

## Algorithms Implemented

| Algorithm      | Best Case  | Average Case | Worst Case |
| -------------- | ---------- | ------------ | ---------- |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      |

## Future Enhancements

* Additional sorting algorithms
* Graph algorithms visualization
* Pathfinding visualizations
* User progress tracking
* Dark mode support
* Algorithm comparison mode

## Author

**Saanvi Srivastava**

GitHub: https://github.com/SaanviS1123
