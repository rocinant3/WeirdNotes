import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from config.database import create_tables
from routers.account import router as account_router
from exceptions.base import BaseExceptionCase
from exceptions.handlers import (
    http_exception_handler,
    request_validation_exception_handler,
    app_exception_handler
)


app = FastAPI()


@app.on_event('startup')
def startup():
    create_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


@app.exception_handler(BaseExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(account_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
