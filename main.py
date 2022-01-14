from fastapi import FastAPI
# from routes.user import user_router
# from routes.login import login_router

app = FastAPI()
# app.include_router(user_router)
# app.include_router(login_router)


@app.get("/")
async def read_data():
    return "ygfreuvrve"
