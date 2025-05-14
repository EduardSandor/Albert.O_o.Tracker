import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_hard_to_guess_string')

    # Database URI for PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://eduard_sandor:IONCuvaca2025@localhost/eduard_sandor_db')

    # Disable Flask-SQLAlchemy track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt_secret_key')
