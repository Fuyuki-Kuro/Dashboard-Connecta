from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
auth_router = APIRouter()

templates = Jinja2Templates(directory="frontend_api/fluxos/auth")
@auth_router.post("/login")
async def login():
    pass

@auth_router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})