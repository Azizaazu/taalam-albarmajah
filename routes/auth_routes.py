#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400
    
    db = get_db()
    if db.users.find_one({'username': username}):
        return jsonify({'error': 'Username already exists!'}), 400
    
    hashed_password = generate_password_hash(password)
    db.users.insert_one({'username': username, 'password': hashed_password})
    
    return jsonify({'message': 'User registered successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400
    
    db = get_db()
    user = db.users.find_one({'username': username})
    
    if user is None or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials!'}), 400
    
    return jsonify({'message': 'Login successful!'}), 200
