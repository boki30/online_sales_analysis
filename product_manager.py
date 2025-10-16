# product_manager.py
from typing import List
from product import Product

class ProductManager:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        # Pretpostavljamo da su imena jedinstvena.
        self.products.append(product)

    def display_products(self) -> None:
        if not self.products:
            print("Nema proizvoda.")
            return
        print("=== Lista proizvoda ===")
        for p in self.products:
            print(p.info())

    def total_inventory_value(self) -> float:
        return sum(p.price * p.quantity for p in self.products)