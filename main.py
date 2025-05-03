from fastapi import FastAPI, Request, APIRouter
from backend_api.colaborators.routes import colaborators_router
app = FastAPI()

app.include_router(colaborators_router, prefix="/colaborators", tags=["colaborators", 'frontend'])
