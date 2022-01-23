import uvicorn
# import typer
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
from routes.login import login_router
from routes.seh import seh_router
from routes.hodim import hodim_router
from routes.user import user_router
from routes.olchov import olchov_router
from routes.homashyo import homashyo_router
from routes.tests import test_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.route('/{_:path}')
# async def https_redirect(request: Request):
#     return RedirectResponse(request.url.replace(scheme='https'))

if __name__ == '__main__':
    uvicorn.run('https_redirect:app', port=80, host='https://oqsaroy.crud.uz')

app.include_router(user_router)
app.include_router(login_router)
app.include_router(seh_router)
app.include_router(hodim_router)
app.include_router(olchov_router)
app.include_router(homashyo_router)
app.include_router(test_router)

@app.get("/")
async def read_data():
    return "Oq saroy projecti"
  
