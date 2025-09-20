from typing import Text
from sqlalchemy import Column, Integer, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ormopt_part2.models.base import Base

class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column()
    store_id: Mapped[int] = mapped_column()
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    rentals: Mapped[list['Rental']] = relationship('Rental', back_populates='rented_inventory')