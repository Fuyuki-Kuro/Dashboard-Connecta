from fastapi import FastAPI, Request, APIRouter
from backend_api.colaborators.routes import colaborators_router
from backend_api.auth.routes import auth_router
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(colaborators_router, tags=["colaborators", 'frontend'])
app.include_router(auth_router, tags=["auth", 'frontend'])
