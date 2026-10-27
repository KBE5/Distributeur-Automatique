#from contextlib import asynccontextmanager
from fastapi import FastAPI

#from api.database import init_db
from api.routers import product
from api.routers import vending_machine


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     init_db()
#     yield
    
app = FastAPI(title="SQLAlchemy - Distributeur-Automatique (mémoire)", version="1.0.0")

app.include_router(product.router)
app.include_router(vending_machine.router)