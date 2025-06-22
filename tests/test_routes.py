import pytest

from main import app

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize('path', ['/', '/favicon.ico', '/screenshot.png', '/robots.txt'])
def test_routes_ok(client, path):
    response = client.get(path)
    assert response.status_code == 200
