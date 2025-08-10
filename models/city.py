from typing import Text
from sqlalchemy import Column, Integer, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ormopt.models.base import Base
from ormopt.models.country import Country

class City(Base):
    __tablename__ = 'city'
    city_id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(Text)
    country_id: Mapped[int] = mapped_column(ForeignKey('country.country_id'))
    located_country: Mapped['Country'] = relationship(back_populates='cities')
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 
    addresses: Mapped[list['Address']] = relationship(back_populates='city')