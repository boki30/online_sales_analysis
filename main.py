# main.py (verzija na grani add-cart-functionality)
import random
from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    pm = ProductManager()

    # Dodaj nekoliko proizvoda
    pm.add_product(Product("Laptop", 1200.0, 5))
    pm.add_product(Product("Phone", 800.0, 10))
    pm.add_product(Product("Headphones", 150.0, 20))
    pm.add_product(Product("Monitor", 300.0, 7))
    pm.add_product(Product("Mouse", 25.0, 50))

    # I dalje: Prikaz liste i inventara (kasnije će main grana brisati ove linije)
    pm.display_products()
    total_value = pm.total_inventory_value()
    print(f"\nUkupna vrednost inventara: {total_value:.2f}\n")

    # Nova funkcionalnost: Korpa
    cart = Cart()

    # Izaberi 3 nasumična proizvoda iz dostupnih
    count = min(3, len(pm.products))
    selected = random.sample(pm.products, count)

    # Dodaj po 1 komad od svakog izabranog proizvoda
    for prod in selected:
        cart.add_product(prod, 1)

    # Prikaz sadržaja korpe i ukupne vrednosti za naplatu
    cart.show_cart()
    print(f"\nUkupno za naplatu: {cart.calculate_total():.2f}")

if __name__ == "__main__":
    main()