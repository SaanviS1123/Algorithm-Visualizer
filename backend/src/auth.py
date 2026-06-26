from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user
from models.user import User, db
from email_service import send_signup_email

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # Validation
    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    # Create user
    user = User(username=username, email=email)
    user.set_password(password)
    
    db.session.add(user)
    db.session.commit()
    
    # Send email notification
    send_signup_email(username, email)
    
    login_user(user)
    
    return jsonify({
        'message': 'Signup successful!',
        'user': {'id': user.id, 'username': user.username, 'email': user.email}
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    login_user(user)
    
    return jsonify({
        'message': 'Login successful!',
        'user': {'id': user.id, 'username': user.username, 'email': user.email}
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({
            'user': {
                'id': current_user.id,
                'username': current_user.username,
                'email': current_user.email
            }
        }), 200
    else:
        return jsonify({'error': 'Not authenticated'}), 401
    
@auth_bp.route('/all-users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for user in users
    ]
    return jsonify({'users': user_list}), 200