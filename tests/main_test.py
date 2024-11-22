import pytest
from fastapi.testclient import TestClient
from app.main import app
from typing import Union
from fastapi import HTTPException

client = TestClient(app)

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200

def test_welcome_message():
    response = client.get("/")
    assert response.json() == {"Message": "Welcome to my ecommerce API!"}

def test_products():
    response = client.get("/products")
    assert response.status_code == 200

def test_length_products():
    response = client.get("/products")
    assert len(response.json()) == 3

def test_product_id():
    response = client.get("/products/1")
    assert response.status_code == 200

def test_product_id1():
    response = client.get("/products/1")
    assert response.json()["id"] ==1

def test_product_id_error_message():
    response = client.get("/products/4")
    assert response.status_code == 404
    assert response.json() == {"detail": {"Status": 404, "Message": "Product not found!"}}

