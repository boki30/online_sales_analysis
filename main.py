# main.py
from product import Product
from product_manager import ProductManager

def main():
    pm = ProductManager()

    # Dodaj nekoliko proizvoda (primer)
    pm.add_product(Product("Laptop", 1200.0, 5))
    pm.add_product(Product("Phone", 800.0, 10))
    pm.add_product(Product("Headphones", 150.0, 20))

    # Prikaz proizvoda
    pm.display_products()

    # Prikaz ukupne vrednosti inventara
    total_value = pm.total_inventory_value()
    print(f"\nUkupna vrednost inventara: {total_value:.2f}")

if __name__ == "__main__":
    main()