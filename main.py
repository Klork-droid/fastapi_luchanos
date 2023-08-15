import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from api.handlers import user_router

app = FastAPI(title='fastapi-luchanos')

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/user', tags=['user'])
main_api_router.include_router(user_router, prefix='/login', tags=['login'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
