from typing import Text
from sqlalchemy import Column, Integer, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ormopt.models.base import Base
from ormopt.models.inventory import Inventory

class Rental(Base):
    __tablename__ = 'rental'
    rental_id: Mapped[int] = mapped_column(primary_key=True)
    rental_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    inventory_id: Mapped[int] = mapped_column(ForeignKey('inventory.inventory_id'))
    customer_id: Mapped[int] = mapped_column()
    return_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    staff_id: Mapped[int] = mapped_column()
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    rented_inventory: Mapped['Inventory'] = relationship('Inventory', back_populates='rentals')
