# Configuration settings for Mini Dynamo

import os

class Config:
    """Configuration class to hold settings for the application."""
    
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    # Add other configuration variables as needed