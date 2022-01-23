from fastapi import APIRouter, Depends
from db import conn  # bazadegi conn chaqiryapmiz
from models.olchov import Olchov, olchov # modelni chaqiryapmiz
from models.user import User # modelni chaqiryapmiz
from .login import get_current_active_user

olchov_router = APIRouter()

# GET qilish
@olchov_router.get("/olchovlar")
async def read_data(current_user: User = Depends(get_current_active_user)):
    return conn.execute(olchov.select()).fetchall()
    
@olchov_router.post("/olchov/create")
async def write_data(new_seh: Olchov, current_user: User = Depends(get_current_active_user)):
    
    count_name = conn.execute(olchov.select().where(olchov.c.name == new_seh.name)).rowcount
    
    if count_name == 0:
        conn.execute(olchov.insert().values(
            name=new_seh.name,
        ))
        return 'success'
    else: 
        return 'failled'
        
@olchov_router.put("/olchov/update/{id}")
async def update_data(id:int, new_seh: Olchov, current_user: User = Depends(get_current_active_user)):
    count_name = conn.execute(olchov.select().where(olchov.c.name == new_seh.name)).rowcount
    
    if count_name > 1:
        return 'failed'
    else:    
        conn.execute(olchov.update().values(
            name=new_seh.name,
        ).where(olchov.c.id == id))
        return 'success'
   