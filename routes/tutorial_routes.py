#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from models import get_db

tutorial_bp = Blueprint('tutorials', __name__)

@tutorial_bp.route('/create', methods=['POST'])
def create_tutorial():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({'error': 'Title and content are required!'}), 400
    
    db = get_db()
    db.tutorials.insert_one({'title': title, 'content': content})
    
    return jsonify({'message': 'Tutorial created successfully!'}), 201

@tutorial_bp.route('/', methods=['GET'])
def get_tutorials():
    db = get_db()
    tutorials = db.tutorials.find()
    result = [{'title': tutorial['title'], 'content': tutorial['content']} for tutorial in tutorials]
    
    return jsonify(result), 200
