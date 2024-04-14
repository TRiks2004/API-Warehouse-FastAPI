from typing import Any

from sqlalchemy import ForeignKey, String, UUID, Interval, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from uuid import uuid4

class MTBase(DeclarativeBase):
    
    def __init__(self, **kw: Any):
        super().__init__(**kw)
        
class MTRole(MTBase):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    
class MTUser(MTBase):
    __tablename__ = 'user'
    
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, index=True
    )
    
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    
    surname: Mapped[str] = mapped_column(String(length=50), nullable=False)
    
    login: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    
    password_hash: Mapped[str] = mapped_column(String(length=255), nullable=False)
    
    phone: Mapped[str] = mapped_column(String(length=20), nullable=False)
    
    role: Mapped[int] = mapped_column(ForeignKey(MTRole.id), nullable=False)

class MTRack(MTBase):
    __tablename__ = 'rack'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    number: Mapped[int] = mapped_column(nullable=False, unique=True)
    
class MTCell(MTBase):
    __tablename__ = 'cell'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    number: Mapped[int] = mapped_column(nullable=False, unique=True)
    
    rack: Mapped[int] = mapped_column(ForeignKey(MTRack.id), nullable=False)
    
class MTOrder(MTBase):
    __tablename__ = 'order'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    number: Mapped[str] = mapped_column(String(length=255), nullable=False)
    
    customer: Mapped[UUID] = mapped_column(ForeignKey(MTUser.id), nullable=False)
    responsible: Mapped[UUID] = mapped_column(ForeignKey(MTUser.id), nullable=False)
    
    cell: Mapped[int] = mapped_column(ForeignKey(MTCell.id), nullable=False)
    
    storage_period: Mapped[Interval] = mapped_column(nullable=False)
    placement_date: Mapped[DateTime] = mapped_column(nullable=False)
    
    small: Mapped[bool] = mapped_column(nullable=False, default=False)
    