from typing import List, Dict, Union


class ProductClass():
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

    # Functions
    def get_products(self):
        return self.products

    def get_product_id(self, id: int) -> Union[Dict[str, any], None]:
        for product in self.products:
            if product["id"] == id:
                return product
        return None

    def add_product(self, product):
        self.products.append(product)
        return product
