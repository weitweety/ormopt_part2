from typing import Text
from sqlalchemy import Column, Integer, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ormopt_part2.models.base import Base

class Country(Base):
    __tablename__ = 'country'
    country_id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(Text)
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    cities: Mapped[list['City']] = relationship('City', back_populates='located_country')