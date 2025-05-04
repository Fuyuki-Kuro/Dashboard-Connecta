from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
auth_router = APIRouter(tags=["autenticação", 'backend'])

templates = Jinja2Templates(directory="/frontend_api/auth")
@auth_router.post("/login")
async def login():
    pass

@auth_router.get("/login")
async def login():
    return templates.TemplateResponse("login.html", {"request": {}})