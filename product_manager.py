# product_manager.py (dodat metod)
from typing import List
from product import Product

class ProductManager:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
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

    def remove_product_by_name(self, name: str) -> bool:
        """
        Uklanja prvi proizvod sa datim imenom (ne razlikuje velika/mala slova).
        Vraća True ako je uklonjen, False ako nije pronađen.
        """
        for i, p in enumerate(self.products):
            if p.name.lower() == name.lower():
                del self.products[i]
                return True
        return False