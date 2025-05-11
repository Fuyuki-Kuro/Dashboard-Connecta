from fastapi import FastAPI, Request, APIRouter, Depends
from backend_api.colaborators.routes import colaborators_router
from backend_api.auth.routes import auth_router
from fastapi.staticfiles import StaticFiles
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis


app = FastAPI()
@app.on_event("startup")
async def startup():
    cache = redis.from_url('redis://18.118.226.162', port=6379, db=0)
    await FastAPILimiter.init(cache)


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(colaborators_router, tags=["colaborators", 'frontend'], dependencies=[Depends(RateLimiter(times=70, seconds=300))])

app.include_router(auth_router, tags=["auth", 'frontend'], dependencies=[Depends(RateLimiter(times=70, seconds=300))])
