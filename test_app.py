# test_app.py

import pytest
from app import app

@pytest.fixture
def app():
    app = app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

# Add more test functions as needed
