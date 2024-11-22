from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

products: List[Dict[str, any]] = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 3000.00
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 50.00
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 100.00
    }
]

@app.get("/") # Request
def hello_world(): # Response
    return {"Message": "Hello World!"}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return {"Status": 404, "Message": "Product not found!"}


