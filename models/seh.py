from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from typing import Optional
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import meta, conn
from pydantic import BaseModel, Field, validator

seh: Table = Table(
    'seh', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), unique=True),
    
)

class Seh(BaseModel):
    name: Optional[str] = Field(
        None, title="Bu seh nomi avval qo`shilgan!", max_length=25
    )
    @validator('name')
    def validate_name(cls, v):
        return v
        # name_count = conn.execute(seh.select().where(seh.c.name == v)).count()
        
        # return name_count
        
  
