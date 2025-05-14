from app.utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationships
    babies = db.relationship('Baby', backref='parent', lazy=True)
    sleeps = db.relationship('Sleep', backref='owner', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Baby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Baby {self.name}, Parent ID: {self.parent_id}>'

class Sleep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Float, nullable=False)  # Duration in hours
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    def __init__(self, start_time, end_time, duration, user_id):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.user_id = user_id

    def __repr__(self):
        return f'<Sleep {self.start_time} - {self.end_time}, Duration: {self.duration} hours>'
