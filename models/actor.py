from typing import Text
from sqlalchemy import Column, Integer, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ormopt.models.base import Base

class Actor(Base):
    __tablename__ = 'actor'
    actor_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(Text)
    last_name: Mapped[str] = mapped_column(Text)
    last_update: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 