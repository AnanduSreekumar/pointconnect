from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

client = MongoClient("mongodb://localhost:27017/")
db = client['user_db']
users_collection = db['users']


@app.route('/')
def home():
    return jsonify({"message": "Welcome to PointConnect!"})


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    firstname = data.get('first_name')
    lastname = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    if not firstname or not lastname or not email or not password:
        return jsonify({"error": "All fields required"}), 400

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


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = users_collection.find_one({"email": email})
    print(user)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid password"}), 401

    return jsonify({"message": "Login successful!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
