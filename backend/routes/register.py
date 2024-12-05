from flask import Blueprint, request, jsonify
from db import users_collection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

register_bp = Blueprint('register', __name__)


@register_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    firstname = data.get('first_name')
    lastname = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    if not firstname or not lastname or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if users_collection.find_one({"email": email}):
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = {
        "first_name": firstname,
        "last_name": lastname,
        "email": email,
        "password": hashed_password
    }
    users_collection.insert_one(new_user)

    return jsonify({"message": "User registered successfully!"}), 200
