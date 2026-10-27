from api.schemas import MoneyIn, VendingMachineOut
from api.services.vending_machine import VendingMachine
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="", tags=["Distributeur"])

# Instance unique de la machine partagée par toutes les requêtes API
machine = VendingMachine()


@router.get("/products", status_code=200)
def get_products():
    """Liste le catalogue de tous les produits."""
    return machine.get_products()


@router.get("/products/{code}", status_code=200)
def get_single_product(code: str):
    """Affiche les détails d'un produit spécifique."""
    product = machine.get_product(code)
    if not product:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product


@router.get("/machine", response_model=VendingMachineOut, status_code=200)
def get_machine_credit():
    """Affiche le crédit courant disponible dans la machine."""
    return VendingMachineOut(credit=machine.credit)


@router.post("/money", response_model=VendingMachineOut, status_code=status.HTTP_200_OK)
def insert_money(money_in: MoneyIn):
    """Ajoute de l'argent dans le distributeur."""
    try:
        credit = machine.insert_money(money_in.amount)
        return VendingMachineOut(credit=credit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/buy/{code}", status_code=200)
def buy_product(code: str):
    """Achète un produit si les conditions sont remplies (stock et crédit)."""
    try:
        product = machine.buy_product(code)
        return {
            "message": "Achat réussi",
            "product": product,
            "remaining_credit": machine.credit,
        }
    except LookupError as e:
        # Si le produit n'existe pas -> 404 Not Found
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        # Si rupture de stock ou crédit insuffisant -> 400 
        raise HTTPException(status_code=400, detail=str(e))
        
@router.post("/refund", status_code=200)
def refund_credit():
    """Rembourse tout le crédit non dépensé et remet le solde à zéro."""
    refunded_amount = machine.refund()
    return {"remboursé": refunded_amount, "credit": machine.credit}