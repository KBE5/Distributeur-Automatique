from api.services.product import Product

class VendingMachine:
    def __init__(self):
        self.credit = 0
        
        self.products: dict[str, Product] ={
            "A1": Product(code="A1", name="Cola", price=150, stock=5),
            "A2": Product(code="A2", name="Eau", price=100, stock=8),
            "B1": Product(code="B1", name="Chips", price=200, stock=3),
            "B2": Product(code="B2", name="Chocolat", price=180, stock=4),
        }

    def get_products(self) -> list[Product]:
        return list(self.products.values())

    def get_product(self, code: str) -> Product | None:
        return self.products.get(code)

    def insert_money(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("Le montant inséré doit être supérieur à zéro.")
        self.credit += amount 
        return self.credit

    def buy_product(self, code:str) -> Product:
        product = self.get_product(code)
        if not product:
            raise ValueError(f"Produit avec le code {code} non trouvé.")
        
        if self.credit < product.price:
            raise ValueError(f"Crédit insuffisant. Crédit actuel: {self.credit}, Prix du produit: {product.price}.")    
        
        if product.stock <= 0:
            raise ValueError("Produit épuisé.")
        self.credit -= product.price
        product.stock -= 1
        return product

    def refund(self):
        refunded_amount = self.credit
        self.credit = 0
        return refunded_amount
