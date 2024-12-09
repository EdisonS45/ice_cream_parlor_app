from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure the app
app.config.from_mapping(
    SECRET_KEY=os.urandom(24),  # Generate a random secret key
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'new_ice_cream_parlor.db')}",  # Database URI
    SQLALCHEMY_TRACK_MODIFICATIONS=False,  # Disable SQLAlchemy event notifications
)

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path, exist_ok=True)
except OSError as e:
    print(f"Error creating instance folder: {e}")

# Initialize the database
db = SQLAlchemy(app)

# Import the routes and models
from app import routes, models
