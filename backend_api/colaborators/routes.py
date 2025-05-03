from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import Request
templates = Jinja2Templates(directory="/frontend_api/fluxos")
colaborators_router = APIRouter()



@colaborators_router.get("/colaborators")
async def render_colaborators(request: Request):
    return templates.TemplateResponse("base.html", {"request": {request}})