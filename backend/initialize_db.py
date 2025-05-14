# in your_application/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configure your app
    return app
