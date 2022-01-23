from typing import Optional
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from db import meta
from pydantic import BaseModel


hodim: Table = Table(
    'hodim', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), index=True),
    Column('role', String(255), index=True),
    Column('phone', Integer, index=True),
    Column('seh_id', Integer, ForeignKey('seh.id', onupdate="CASCADE", ondelete="CASCADE"), index=True),
    Column('status', Boolean, index=True, default=True),
    Column('salary', Integer, index=True, default=0),
    Column('sana', DateTime),
)

class Hodim(BaseModel):
    name: str
    role: str
    phone: int 
    seh_id: int
