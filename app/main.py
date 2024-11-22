from fastapi import FastAPI, HTTPException
from .schema import ProductSchema, ErrorResponse
from .data import ProductClass
from typing import Union

app = FastAPI()
products_list = ProductClass()

@app.get("/") # Request
def welcome(): # Response
    return {"Message": "Welcome to my ecommerce API!"}

@app.get("/products", response_model = list[ProductSchema])
def get_products():
    return products_list.get_products()

@app.get("/products/{id}", response_model=Union[ProductSchema, ErrorResponse])
def get_product_id(id: int):
    product = products_list.get_product_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail={"Status": 404, "Message": "Product not found!"})
    return product

@app.post("/products", response_model=ProductSchema)
def add_product(product: ProductSchema):
    return products_list.add_product(product)


