from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
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
    "settings": True,
}

@colaborators_router.get("/colaborators")
async def render_colaborators(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "menu": menu})