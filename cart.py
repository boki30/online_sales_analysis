# cart.py
from typing import List, Tuple
from product import Product

class Cart:
    def __init__(self) -> None:
        # Svaka stavka je (Product, quantity)
        self.cart_items: List[Tuple[Product, int]] = []

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Količina mora biti pozitivna.")
        # Ako je proizvod već u korpi, uvećaj količinu
        for idx, (p, q) in enumerate(self.cart_items):
            if p.name.lower() == product.name.lower():
                self.cart_items[idx] = (p, q + quantity)
                return
        self.cart_items.append((product, quantity))

    def calculate_total(self) -> float:
        return sum(p.price * q for p, q in self.cart_items)

    def show_cart(self) -> None:
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("=== Sadržaj korpe ===")
        for p, q in self.cart_items:
            line_total = p.price * q
            print(f"{p.name} x{q} = {line_total:.2f}")