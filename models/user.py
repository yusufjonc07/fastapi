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
    Column('username', String(255), unique=True),
    Column('hashed_password', String(255)),
    Column('hodim_id', Integer),
    Column('token', String(255)),
    Column('disabled', Boolean, default=False),
)


class Token(BaseModel):
    access_token: str
    token_type: str
    role: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    hodim_id: int
    disabled: Optional[bool] = None

class NewUser(BaseModel):
    username: str
    password: str 
    hodim_id: int

class UserInDB(User):
    hashed_password: str

class UserStatus(BaseModel):
    disabled: int



