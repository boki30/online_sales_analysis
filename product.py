# product.py
class Product:
    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        if price < 0:
            raise ValueError("Cena ne može biti negativna.")
        if quantity < 0:
            raise ValueError("Količina ne može biti negativna.")
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def info(self) -> str:
        return f"Proizvod: {self.name} | Cena: {self.price:.2f} | Količina: {self.quantity} | Vrednost: {self.price * self.quantity:.2f}"

    def update_quantity(self, new_quantity: int) -> None:
        if new_quantity < 0:
            raise ValueError("Količina ne može biti negativna.")
        self.quantity = int(new_quantity)

    def __repr__(self) -> str:
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"