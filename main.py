# main.py (konačna verzija posle spajanja i rešavanja konflikta)
import random
from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    pm = ProductManager()

    # Zadržane izmene sa main grane (nova imena/količine)
    pm.add_product(Product("Laptop Pro", 1200.0, 4))
    pm.add_product(Product("Smartphone X", 850.0, 12))
    pm.add_product(Product("Wireless Headphones", 180.0, 18))
    pm.add_product(Product("Monitor", 300.0, 7))
    pm.add_product(Product("Mouse", 25.0, 50))

    # Ne prikazujemo inventar

    # Zadržana funkcionalnost korpe sa add-cart-functionality grane
    cart = Cart()
    count = min(3, len(pm.products))
    selected = random.sample(pm.products, count)
    for prod in selected:
        cart.add_product(prod, 1)

    cart.show_cart()
    print(f"\nUkupno za naplatu: {cart.calculate_total():.2f}")

if __name__ == "__main__":
    main()