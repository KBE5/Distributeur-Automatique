#GET	/machine	Crédit courant
#POST	/money	Ajout d'argent
#Le corps de POST /money est :

#{"amount": 200}
#POST	/buy/{code}	Achat
#POST	/refund	Remboursement du crédit

from fastapi import APIRouter, HTTPException
from api.schemas import VendingMachineOut, MoneyIn
from api.services.vending_machine import VendingMachine


router = APIRouter(prefix="/machine", tags=["Distributeur"])

@router.get("", response_model=VendingMachineOut, status_code=200)
def get_machine():
    """
    Récupère le crédit courant de la machine.
    """

    credit = VendingMachine().credit
    return VendingMachineOut(credit=credit)
