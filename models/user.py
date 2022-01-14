from sqlalchemy import Table, Column
from typing import Optional
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import meta
from pydantic import BaseModel
from fastapi import Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users: Table = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('ism', String(255)),
    Column('hashed_password', String(255), ),
    Column('token', String(255), ),
    Column('username', String(255), unique=True),
    Column('phone', String(255), unique=True),
    Column('role', String(255)),
    Column('seh_id', Integer),
    Column('disabled', Boolean, default=False),
)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    phone: Optional[str] = None
    ism: Optional[str] = None
    disabled: Optional[bool] = None

class NewUser(BaseModel):
    username: str
    password: str = Query(None, min_length=5, max_length=8)
    role: str
    name: str
    phone: str
    seh_id: int



class UserInDB(User):
    hashed_password: str





