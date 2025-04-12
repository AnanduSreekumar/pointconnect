from flask import Blueprint, request, jsonify, redirect, url_for, session
from db import users_collection
from flask_bcrypt import Bcrypt
from oauth import google

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


@register_bp.route('/register/google')
def google_register():
    """
    Redirects the user to Google's OAuth 2.0 authorization page for registration.
    """
    redirect_uri = url_for('register.google_register_callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@register_bp.route('/register/google/callback')
def google_register_callback():
    """
    Handles the callback from Google after user authorization for registration.
    """
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()

    # Check if the user already exists in the database
    user = users_collection.find_one({"email": user_info['email']})
    if user:
        return jsonify({"error": "Email already exists"}), 400

    # Register the user
    new_user = {
        "first_name": user_info.get('given_name'),
        "last_name": user_info.get('family_name'),
        "email": user_info['email'],
        "google_id": user_info['id']
    }
    users_collection.insert_one(new_user)

    # Store user info in session
    session['user'] = user_info
    return jsonify({"message": "User registered successfully via Google!", "user": user_info}), 200
