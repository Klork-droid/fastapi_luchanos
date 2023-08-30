import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

import settings
from api.handlers import user_router
from api.login_handler import login_router
from api.service import service_router

app = FastAPI(title='fastapi-luchanos')

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/user', tags=['user'])
main_api_router.include_router(login_router, prefix='/login', tags=['login'])
main_api_router.include_router(service_router, tags=['service'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=settings.APP_PORT)
