# main.py (modifikovano na main pre merge-a)
from product import Product
from product_manager import ProductManager

def main():
    pm = ProductManager()

    # Izmenjena imena/količine na main grani
    pm.add_product(Product("Laptop Pro", 1200.0, 4))
    pm.add_product(Product("Smartphone X", 850.0, 12))
    pm.add_product(Product("Wireless Headphones", 180.0, 18))

    # Namerno uklonjen prikaz proizvoda i ukupne vrednosti inventara na main grani
    # (radi zadatka i potencijalnog konflikta pri spajanju sa add-cart-functionality)

if __name__ == "__main__":
    main()