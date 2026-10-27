"""Modèles ORM SQLAlchemy : Station, Trajet, Incident, Utilisateur.

Déclarer les quatre tables conformément à sql/schema.sql.
"""

from sqlalchemy import Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from api.database import Base
from typing import List


class Product(Base):
    
    __tablename__ = "product"

    code: Mapped [str] = mapped_column(String(50), primary_key=True)
    name: Mapped [str] = mapped_column(String(100), nullable=False)
    price: Mapped [int] = mapped_column(Integer, nullable=False)
    stock: Mapped [int] = mapped_column(Integer, default=0, nullable=False)

    # Clé étrangère : chaque produit est rattaché à un distributeur
    vending_machine_id: Mapped[int] = mapped_column(ForeignKey("vending_machine.id"), nullable=False)
    

class VendingMachine(Base):
    
    __tablename__ = "vending_machine"

    id: Mapped [int] = mapped_column(Integer, primary_key=True)
    credit: Mapped [int] = mapped_column(Integer, default=0, nullable=False)

    # Relation : Un distributeur possède plusieurs produits
    products: Mapped[List["Product"]] = relationship(back_populates="vending_machine", cascade="all, delete-orphan")