class Product:
    def __init__(self,code:str, name:str, price: int, stock:int):
        self.code = code
        self.name = name
        self.price = price 
        self.stock = stock
    
    def is_available(self) : 
        if self.stock > 0:
            return True 
        else:
            return False
        
    def dispense(self):
        if not self.is_available():
            raise ValueError(f"Le produit {self.name} ({self.code}) est en rupture de stock.")
        else: 
            self.stock -= 1
      