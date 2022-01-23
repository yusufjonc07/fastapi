from fastapi import APIRouter, Response
from typing import Optional
from pydantic import BaseModel, Field

test_router = APIRouter()

@test_router.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}
