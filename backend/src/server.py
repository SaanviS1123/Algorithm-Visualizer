import sys
sys.path.insert(0, '/Users/saanvisrivastava/Downloads/algo-visualizer/backend/src')
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv
import os
from algorithms.bubble_sort import BubbleSort
from algorithms.quick_sort import QuickSort
from algorithms.merge_sort import MergeSort
from algorithms.insertion_sort import InsertionSort
from models.user import db, User
from auth import auth_bp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///algo_visualizer.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

CORS(app, supports_credentials=True)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = jsonify({"status": "ok"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response

@app.route('/api/run-algorithm', methods=['POST', 'OPTIONS'])
def run_algorithm():
    data = request.json
    algorithm = data.get('algorithm')
    dataset = data.get('dataset')
    
    if algorithm == 'bubble-sort':
        sorter = BubbleSort(dataset)
        steps = sorter.execute()
        
        response = jsonify({
            'steps': steps,
            'metrics': sorter.metrics
        })
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
    elif algorithm == 'quick-sort':
        sorter = QuickSort(dataset)
        steps = sorter.execute()
        
        response = jsonify({
            'steps': steps,
            'metrics': sorter.metrics
        })
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
    elif algorithm == 'merge-sort':
        sorter = MergeSort(dataset)
        steps = sorter.execute()
        
        response = jsonify({
            'steps': steps,
            'metrics': sorter.metrics
        })
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
    elif algorithm == 'insertion-sort':
        sorter = InsertionSort(dataset)
        steps = sorter.execute()
        
        response = jsonify({
            'steps': steps,
            'metrics': sorter.metrics
        })
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
    return jsonify({'error': 'Algorithm not found'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)