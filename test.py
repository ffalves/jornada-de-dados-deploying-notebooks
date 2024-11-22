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

def test_products():
    response = client.get("/products")
    assert response.status_code == 200

def test_length_products():
    response = client.get("/products")
    assert len(response.json()) == 3

