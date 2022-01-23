from fastapi import APIRouter, Depends, HTTPException
from db import conn  # bazadegi conn chaqiryapmiz
from models.user import users, NewUser, User, UserStatus # modelni chaqiryapmiz
from models.hodim import hodim # modelni chaqiryapmiz
from .login import get_password_hash, get_current_active_user

user_router = APIRouter()

# GET qilish
@user_router.get("/users")
async def read_data(current_user: User = Depends(get_current_active_user)):
    return conn.execute(users.select().where(users.c.disabled == False)).fetchall()
    # return "fhrgnmv"
    
# GET qilish
@user_router.get("/users_block")
async def read_data(current_user: User = Depends(get_current_active_user)):
    return conn.execute(users.select().where(users.c.disabled == True)).fetchall()
    # return "fhrgnmv"


# # # id bilan GET qilish
@user_router.get("/user/{id}")
async def this_get_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchone()


# # POST method
@user_router.post("/user/create")
async def write_data(user_data: NewUser, current_user: User = Depends(get_current_active_user)):
    
    #validate username
    count_username = conn.execute(users.select().where(users.c.username == user_data.username)).rowcount
    count_hodim = conn.execute(users.select().where(users.c.hodim_id == user_data.hodim_id)).rowcount
    is_hodim = conn.execute(hodim.select().where(hodim.c.id == user_data.hodim_id)).rowcount
    
    if is_hodim == 0:
        raise HTTPException(status_code=404, detail="Bunday hodim mavjud emas!")
    elif count_username > 0 or count_hodim > 0:
        raise HTTPException(status_code=404, detail="Bu user avval ro`yxatga olingan!")
    elif len(user_data.username) < 5 or len(user_data.password) < 8:
        raise HTTPException(status_code=404, detail="Login yoki parolni to`g`ri kiriting!")
    else:
        
        conn.execute(users.insert().values(
            username=user_data.username,
            hashed_password=get_password_hash(user_data.password),
            hodim_id=user_data.hodim_id,
        ))
        return "success"
  
 # POST method
@user_router.put("/user/update/{id}")
async def write_data(id:int, user_data: NewUser, current_user: User = Depends(get_current_active_user)):
    
    #validate username
    this_user = conn.execute(users.select().where(users.c.id == id)).fetchone()
    count_username = conn.execute(users.select().where(users.c.username == user_data.username)).rowcount
    count_hodim = conn.execute(users.select().where(users.c.hodim_id == user_data.hodim_id)).rowcount
    is_hodim = conn.execute(hodim.select().where(hodim.c.id == user_data.hodim_id)).rowcount
    
    if this_user:
        if is_hodim == 0:
            raise HTTPException(status_code=404, detail="Bunday hodim mavjud emas!")
        elif count_username > 1 or count_hodim > 1:
            raise HTTPException(status_code=404, detail="Bu user avval ro`yxatga olingan!")
        elif len(user_data.username) < 5 or len(user_data.password) < 8:
            raise HTTPException(status_code=404, detail="Login yoki parolni to`g`ri kiriting!")
        else:
            
            conn.execute(users.update().values(
                username=user_data.username,
                hashed_password=get_password_hash(user_data.password),
                hodim_id=user_data.hodim_id,
            ).where(users.c.id == id))
            return "success"
    else:
        raise HTTPException(status_code=404, detail="Bunday user mavjud emas!")
#
# # # id bilan GET qilish
@user_router.get("/user_block/{id}")
async def this_gett_user(id: int, current_user: User = Depends(get_current_active_user)):
    conn.execute(users.update().values(disabled=True).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).fetchone()
# # # id bilan GET qilish
@user_router.get("/user_open/{id}")
async def this_gett_user(id: int, current_user: User = Depends(get_current_active_user)):
    conn.execute(users.update().values(disabled=False).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).fetchone()

