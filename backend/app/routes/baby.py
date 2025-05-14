from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.db import db  # Corrected import
from ..models import User  # Corrected import

bp = Blueprint('user', __name__, url_prefix='/api/user')

@bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    if user:
        return jsonify({
            'username': user.username,
            'email': user.email
        })
    return jsonify({'message': 'User not found'}), 404

@bp.route('/update', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    db.session.commit()

    return jsonify({'message': 'Profile updated successfully'})
