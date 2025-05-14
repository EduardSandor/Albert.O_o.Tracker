from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from app import db
from app.models import Sleep, Baby

sleep_bp = Blueprint('sleep', __name__)

@sleep_bp.route('/add_sleep_data', methods=['POST'])
@jwt_required()
def add_sleep_data():
    data = request.get_json()
    start_time_str = data.get('startTime')
    end_time_str = data.get('endTime')
    comments = data.get('comments')
    baby_id = data.get('babyId')

    if not start_time_str or not end_time_str or not baby_id:
        return jsonify({'error': 'Start time, end time, and baby ID are required'}), 400

    try:
        start_time = datetime.fromisoformat(start_time_str)  # Assuming ISO 8601 format
        end_time = datetime.fromisoformat(end_time_str)      # Assuming ISO 8601 format
    except ValueError:
        return jsonify({'error': 'Invalid datetime format'}), 400

    new_sleep_data = Sleep(
        start_time=start_time,
        end_time=end_time,
        duration=(end_time - start_time).total_seconds() / 3600,  # Duration in hours
        user_id=get_jwt_identity()['id']  # Assuming JWT identity contains user ID
    )
    db.session.add(new_sleep_data)
    db.session.commit()

    return jsonify({
        'id': new_sleep_data.id,
        'start_time': new_sleep_data.start_time.isoformat(),
        'end_time': new_sleep_data.end_time.isoformat(),
        'comments': new_sleep_data.comments,
        'duration': new_sleep_data.duration
    }), 201

@sleep_bp.route('/get_sleep_data', methods=['GET'])
@jwt_required()
def get_sleep_data():
    bab
