from fastapi import APIRouter, Depends
from db import conn  # bazadegi conn chaqiryapmiz
from models.user import users, User, NewUser # modelni chaqiryapmiz
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

user_router = APIRouter()

# GET qilish
@user_router.get("/users")
async def read_data():
    return conn.execute(users.select()).fetchall()




# # id bilan GET qilish
@user_router.get("/user/{idd}")
async def read_data(idd: int):
    return conn.execute(users.select().where(users.c.id == idd)).fetchall()


# # POST method
@user_router.post("/user/create")
async def write_data(new_user: NewUser):
    return conn.execute(users.insert().values(
        ism=new_user.ism,
        password=new_user.password,
        username=new_user.username,
        phone=new_user.phone,
    ))
    return conn.execute(users.select()).fetchall()

#
# # PUT method
# @user.put("user/{id}")
# async def update_data(id: int, user: User):
#     conn.execute(users.update().values(
#         name=user.name,
#         phone=user.phone,
#         adress=user.adress
#     ).where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()

#
# # DELETE method
# @user.delete("user/{id}")
# async def delete_data(id: int):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()

