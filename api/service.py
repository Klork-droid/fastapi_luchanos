from fastapi import APIRouter

service_router = login_router = APIRouter()


@service_router.get('/ping')
async def ping():
    return {'Success': True}


@service_router.get('/sentry-debug')
async def trigger_error():
    raise ValueError
