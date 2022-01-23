from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import meta, conn, Base, engine
from pydantic import BaseModel, Field, validator
from sqlalchemy.orm import relationship

homashyo: Table = Table(
    'homashyo', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), unique=True),
    Column('olchov_id', Integer)
)

class Olchov(Base):
    __tablename__ = 'olchov'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    homs = relationship("Homashyoo", back_populates='the_olchov')
    
class Homashyoo(Base):
    __tablename__ = 'homashyo'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    olchov_id = Column(Integer, nullable=False, ForeignKey("olchov.id"))
    the_olchov = relationship("Olchov",  back_populates='homs')

class Homashyo(BaseModel):
    name: str
    olchov_id: int
    
Base.metadata.create_all(engine)
  
