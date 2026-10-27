from fastapi import APIRouter, HTTPException
from api.schemas import ProductOut
from api.services.vending_machine import VendingMachine

router = APIRouter(prefix="/products", tags=["Produits"])

@router.get("", response_model=list[ProductOut], status_code=200)
def get_products():
    """
    Récupère la liste de tous les produits en mémoire (dictionnaire en dur).
    """
    machine = VendingMachine()
    return machine.get_products()

@router.get("/{code}", response_model=ProductOut, status_code=200)
def get_product(code: str):
    """
    Récupère les détails d'un produit spécifique via son code dans le dictionnaire.
    """
    machine = VendingMachine()
    product = machine.get_product(code)
    if not product:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product