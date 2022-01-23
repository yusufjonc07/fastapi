from fastapi import APIRouter, Depends
from db import conn  # bazadegi conn chaqiryapmiz
from models.homashyo import Homashyo, Homashyoo, homashyo # modelni chaqiryapmiz
from models.olchov import olchov # modelni chaqiryapmiz
from models.user import User # modelni chaqiryapmiz
from .login import get_current_active_user

homashyo_router = APIRouter()

# GET qilish
@homashyo_router.get("/homashyolar")
async def read_data(current_user: User = Depends(get_current_active_user)):
    return conn.execute(homashyo.select()).fetchall()
    # homashyos = []
    # for hom in homashyolar:
    #     the_olchov = conn.execute(olchov.select().where(olchov.c.id == hom.olchov_id)).fetchone()
    #     homashyos.append({
    #         id:hom.id,
    #         name:hom.name,
    #         olchov:the_olchov.name,
    #     })
        
    # return homashyos
    
@homashyo_router.post("/homashyo/create")
async def write_data(new_seh: Homashyo, current_user: User = Depends(get_current_active_user)):
    
    count_name = conn.execute(homashyo.select().where(homashyo.c.name == new_seh.name)).rowcount
    
    if count_name == 0:
        conn.execute(homashyo.insert().values(
            name=new_seh.name,
            olchov_id=new_seh.olchov_id,
        ))
        return 'success'
    else: 
        return 'failled'
        
@homashyo_router.put("/homashyo/update/{id}")
async def update_data(id:int, new_seh: Homashyo, current_user: User = Depends(get_current_active_user)):
    count_name = conn.execute(homashyo.select().where(homashyo.c.name == new_seh.name)).rowcount
    
    if count_name > 1:
        return 'failed'
    else:    
        conn.execute(homashyo.update().values(
            name=new_seh.name,
            olchov_id=new_seh.olchov_id,
        ).where(homashyo.c.id == id))
        return 'success'
   