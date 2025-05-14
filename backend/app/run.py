from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.app.utils.config import Config
from backend.app.utils.db import db
from backend.app.models import User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Apply CORS to the app
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400

    # Create new user
    new_user = User(email=email)
    new_user.set_password(password)  # Assuming User model has set_password method
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True, host='0.0.0.0', port=5000)
