import requests

def test_mock_sqrt_64():
    response = requests.get("http://localhost:8081/calc/sqrt/64")
    assert response.status_code == 200
    assert response.text.strip() == "8"