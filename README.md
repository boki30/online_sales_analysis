# Online Sales Analysis

Projekat simulira osnovni sistem upravljanja proizvodima i korpom kupca korišćenjem OOP koncepata u Pythonu i Git/GitHub rada sa granama, spajanjem i rešavanjem konflikata.

## Struktura
- `product.py` — Klasa `Product` (name, price, quantity), `info()`, `update_quantity()`.
- `product_manager.py` — Klasa `ProductManager` sa listom proizvoda, metodima za dodavanje, prikaz i ukupnu vrednost inventara, kao i `remove_product_by_name()`.
- `cart.py` — Klasa `Cart` sa dodavanjem proizvoda, prikazom sadržaja i obračunom ukupne vrednosti.
- `main.py` — Ulazna tačka: pravi proizvode, prikazuje i radi sa korpom (posle spajanja grana).
- `.gitignore` — Ignorisanje `config.json` i screenshotova.
- `screenshots/` — Snimci ekrana (ignorisan folder).
- `config.json` — Primer poverljivih podataka (ignorisan).

## Kako pokrenuti
```bash
python main.py
# ili
python3 main.py