from fastapi import APIRouter, Depends
from db import conn  # bazadegi conn chaqiryapmiz
from models.hodim import Hodim, hodim # modelni chaqiryapmiz
from models.user import User # modelni chaqiryapmiz
from .login import get_current_active_user

hodim_router = APIRouter()

# GET qilish
@hodim_router.get("/hodimlar")
async def read_data(current_user: User = Depends(get_current_active_user)):
    return conn.execute(hodim.select()).fetchall()
    
@hodim_router.post("/hodim/create")
async def read_data(new_hodim: Hodim, current_user: User = Depends(get_current_active_user)):
    conn.execute(hodim.insert().values(
        name=new_hodim.name,
        role=new_hodim.role,
        phone=new_hodim.phone,
        seh_id=new_hodim.seh_id
    ))
    
    return conn.execute(hodim.select()).fetchall()
    
@hodim_router.put("/hodim/update/{id}")
async def read_data(id:int, new_hodim: Hodim, current_user: User = Depends(get_current_active_user)):
    
    this_hodim = conn.execute(hodim.select().where(hodim.c.id == id)).fetchone()
    
    if this_hodim:
        conn.execute(hodim.update().values(
            name=new_hodim.name,
            role=new_hodim.role,
            phone=new_hodim.phone,
            seh_id=new_hodim.seh_id
        ).where(hodim.c.id == id))
    
        return conn.execute(hodim.select().where(hodim.c.id == id)).fetchone()
   