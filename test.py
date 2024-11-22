import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200

def test_hello_world_message():
    response = client.get("/")
    assert response.json() == {"Message": "Hello World!"}