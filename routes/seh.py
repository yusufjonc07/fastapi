from fastapi import APIRouter, Depends
from db import conn  # bazadegi conn chaqiryapmiz
from models.seh import Seh, seh # modelni chaqiryapmiz
from models.user import User # modelni chaqiryapmiz
from .login import get_current_active_user

seh_router = APIRouter()

# GET qilish
@seh_router.get("/sehlar")
async def read_data(current_user: User = Depends(get_current_active_user)):
    return conn.execute(seh.select()).fetchall()
    
@seh_router.post("/seh/create")
async def read_data(new_seh: Seh, current_user: User = Depends(get_current_active_user)):
    conn.execute(seh.insert().values(
        name=new_seh.name,
    ))
    
    return conn.execute(seh.select()).fetchall()
   