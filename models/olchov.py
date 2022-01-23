from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from typing import Optional
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import meta, conn
from pydantic import BaseModel, Field, validator

olchov: Table = Table(
    'olchov', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), unique=True),
)

class Olchov(BaseModel):
    name: str
  
