from fastapi import APIRouter, Request, Depends, HTTPException, status, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from backend_api.security.security_roles import validate_token, create_access_token, verify_password, limiter
from datetime import datetime
from bson.objectid import ObjectId

def define_menu(user_type):    
     # Defina o menu conforme o tipo
    if user_type == "Admin":
        menu = {
            "dashboard": True,
            "calendar": True,
            "equipe": True,
            "contratos": True,
            "projetos": True,
            "pagamentos": True,
            "tickets": True
        }
        return menu
    
    elif user_type == "funcionario":
        menu = {
            "dashboard": True,
            "calendar": True,
            "equipe": False,
            "projetos": True,
            "pagamentos": True,
            "tickets": True
        }
        return menu
    
    else:  # cliente
        menu = {
            "dashboard": True,
            "calendar": False,
            "equipe": False,
            "projetos": True,
            "pagamentos": False,
            "tickets": False
        }
        return menu

projects = []
postagens = []
ticket = []

def datetimeformat(value, format="short"):
    if not value:
        return ""
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value)
        except ValueError:
            return value
    if format == "short":
        return value.strftime("%d/%m/%Y")
    elif format == "time":
        return value.strftime("%H:%M")
    elif format == "full":
        return value.strftime("%d/%m/%Y %H:%M")
    else:
        return value.strftime(format)

user_info = {
    "_id": ObjectId(),
    "user": {
        "nome": "Leonard Henrique",
        "username": "leonard_connecta",
        "cpf": "12345678900",
        "rg": "12345678-9",
        "email": "leonard@xpto.com",
        "tipo": "funcionario",
        "cargo": "Designer",
        "senha": "777-Rroot"
    },
    "tickets": [],
    "contracts_info": [],
    "services_info": [],
    "status": "PENDENTE",
    }

user_data = user_info["user"]

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
    templates = Jinja2Templates(directory="frontend_api/fluxos/colaborators/templates/")

    templates.env.filters["datetimeformat"] = datetimeformat


    projetos_ativos = sum(1 for p in projects if p["status"] == "em andamento")
    total_postagens = len([p for p in postagens if p["status"] != "cancelada"])
    postagens_previstas = 16
    percentual_postagens = round((total_postagens / postagens_previstas) * 100) if postagens_previstas else 0

    faturamento_atual = 5200
    meta_faturamento = 8000
    percentual_faturamento = round((faturamento_atual / meta_faturamento) * 100) if meta_faturamento else 0

    tickets_pendentes = len([t for t in ticket if t["status"] == "pendente"])

    hoje = datetime.now()
    proximas_entregas = []
    for projeto in projects:
        for entrega in projeto["entregas"]:
            data_entrega = datetime.fromisoformat(entrega["data"])
            if data_entrega >= hoje:
                proximas_entregas.append({
                    "data": data_entrega,
                    "descricao": entrega["descricao"]
                })

    user_safe = {
        "name": user_data["nome"],
        "type": user_data["tipo"],
        "role": user_data["cargo"]   
    }
    proximas_entregas.sort(key=lambda x: x["data"])
    return templates.TemplateResponse("dashboard.html", {"request": request, "menu": menu, "request": request,
        "user": user_safe,
        "menu": define_menu(user_safe["type"]),
        "projects_count": projetos_ativos,
        "postagens_count": total_postagens,
        "postagens_percent": percentual_postagens,
        "faturamento_valor": f"R${faturamento_atual:,.0f}".replace(",", "."),
        "faturamento_percent": percentual_faturamento,
        "tickets_pendentes": tickets_pendentes,
        "proximas_entregas": proximas_entregas,})
