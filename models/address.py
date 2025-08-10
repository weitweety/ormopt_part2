from typing import Text
from sqlalchemy import Column, Integer, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ormopt.models.base import Base
from ormopt.models.city import City

class Address(Base):
    __tablename__ = 'address'
    address_id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(Text)
    address2: Mapped[str] = mapped_column(Text)
    district: Mapped[str] = mapped_column(Text)
    city_id: Mapped[int] = mapped_column(ForeignKey('city.city_id'))
    city: Mapped['City'] = relationship(back_populates='addresses')