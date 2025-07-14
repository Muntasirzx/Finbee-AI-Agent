# app/__init__.py

from flask import Flask

# Create the main Flask application instance
app = Flask(__name__)

# Import the routes to register them with the Flask app
# This is placed at the bottom to avoid circular import errors.
from app import routes

