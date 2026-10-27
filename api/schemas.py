from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    code: str = Field(..., max_length=50)
    name: str = Field(..., max_length=100)
    price: int
    stock: int = 0

class ProductUpdate(ProductCreate):
    pass

class ProductOut(ProductCreate):
    pass


class VendingMachineCreate(BaseModel):
    credit: int = 0

class VendingMachineOut(VendingMachineCreate):
    pass

class MoneyIn(BaseModel):
    amount: int = Field(..., gt=0)

