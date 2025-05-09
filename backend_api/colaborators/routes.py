from fastapi import APIRouter, Request, Depends, HTTPException, status, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from backend_api.security.security_roles import validate_token, create_access_token, verify_password, limiter


templates = Jinja2Templates(directory="frontend_api/fluxos")

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

@colaborators_router.get("/dashboard")
async def render_dashboard(request: Request):
    templates = Jinja2Templates(directory="frontend_api/fluxos/colaborators/templates")
    return templates.TemplateResponse("dashboard.html", {"request": request, "menu": menu})
