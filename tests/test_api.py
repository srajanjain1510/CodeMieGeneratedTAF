import requests

class TestAPI:
    def test_example(self):
        response = requests.get('http://localhost:5000/example')
        assert response.status_code == 200
