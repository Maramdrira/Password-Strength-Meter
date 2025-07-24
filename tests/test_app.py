from password_strength_checker import check_strength
from password_strength_checker.app import app

def test_check_strength():
    # Setup test config
    app.config['MIN_WEAK'] = 6
    app.config['MIN_STRONG'] = 10
    app.config['SPECIAL_CHARS'] = "!@#$%^&*"
    
    assert check_strength("123") == "Weak 🚨"
    assert check_strength("1234567") == "Medium ⚠️"
    assert check_strength("StrongPass123!") == "Strong ✅"

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200