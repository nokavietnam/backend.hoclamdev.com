import os
import sys

# Add the directory containing the application to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the application object from app.py
from app import app as application