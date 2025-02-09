import requests

def test_example():
    response = requests.get("https://cataas.com/api/cats")
    assert response.status_code == 200
