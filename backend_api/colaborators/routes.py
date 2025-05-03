from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import Request
templates = Jinja2Templates(directory="/frontend_api/fluxos")
colaborators_router = APIRouter()

menu = {
    "dashboard": True,
    "calendar": True,
    "work_materials": True,
    "services": True,
    "service": True, 
    "contracts": True,
    "tickets": True,
    "teams": True,
    "clients": True,
    "users": True,
    "settings": True
}


@colaborators_router.get("/colaborators")
async def render_colaborators(request: Request):
    return templates.TemplateResponse("base.html", {"request": {request}, "menu": menu})