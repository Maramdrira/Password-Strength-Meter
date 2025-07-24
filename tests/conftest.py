import os
import sys
from pathlib import Path
import pytest

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from password_strength_checker.app import app as flask_app

@pytest.fixture
def app():
    # Set the template folder explicitly for tests
    flask_app.template_folder = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        '../templates'
    )
    flask_app.config['TESTING'] = True
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()