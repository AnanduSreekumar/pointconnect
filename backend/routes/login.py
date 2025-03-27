from flask import Blueprint, request, jsonify
from db import users_collection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    user = users_collection.find_one({"email": email})

    if not user:
        return jsonify({"error": "Email doesn't exists"}), 400

    if not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid password"}), 400

    return jsonify({"message": "Login successful!"}), 200
