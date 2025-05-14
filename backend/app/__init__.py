from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.utils.config import Config
from app.utils.db import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Initialize migration tools
    migrate.init_app(app, db)

    # Initialize CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Register blueprints
    from app.routes.auth import bp as auth_bp
    from app.routes.user import bp as user_bp
    from app.routes.baby import bp as baby_bp
    from app.routes.sleep import bp as sleep_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(baby_bp)
    app.register_blueprint(sleep_bp)

    return app
