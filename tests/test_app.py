from password_strength_checker.app import app, check_strength

def test_check_strength():
    assert check_strength("123") == "Weak 🚨"
    assert check_strength("1234567") == "Medium ⚠️"
    assert check_strength("StrongPass123!") == "Strong ✅"

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200