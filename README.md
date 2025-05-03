# Dashboard-Connecta
🇧🇷 PT-BR: Dashboard para agências de marketing de médio e grande porte. Gerencie equipes, clientes e campanhas com métricas em tempo real. Interface responsiva, suporte a temas e integração com MongoDB. Desenvolvido com Python, FastAPI, Jinja2, HTML, CSS e JS.

# 🚀 Sistema Web com FastAPI + Jinja2

Projeto web estruturado com FastAPI (backend) e Jinja2/HTML/CSS (frontend) com suporte a temas (dark/light), autenticação JWT, usuários com perfis de cliente e administrador, e estrutura modular organizada para escalabilidade.

---

### 📁 Project Structure

```text
.
├── main.py
├── .env
├── database.py
├── .gitignore
├── README.md

├── backend_api/
│   ├── auth/
│   │   ├── routes.py
│   │   └── services.py
│   │
│   ├── security/
│   │   └── security.py
│   │
│   ├── clientes/
│   │   ├── routes.py                # /clientes, /clientes/servicos, /clientes/contratos
│   │   ├── services.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── administradores/
│   │   ├── routes.py                # /admin/usuarios, /admin/equipe, /admin/contratos
│   │   ├── services.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   └── arquivos/
│       ├── routes.py                # /upload, /download, /clientes/{id}/anexos
│       ├── services.py
│       └── storage.py               # Salvar, listar, remover arquivos

├── frontend_api/
│   ├── auth/
│   │   └── views.py
│   │
│   └── fluxos/
│       ├── base.html
│       ├── base.css
│       ├── theme_dark.css
│       ├── theme_light.css
│
│       ├── funcionarios/
│       │   ├── templates/
│       │   │   ├── dashboard.html
│       │   │   ├── calendar.html
│       │   │   ├── work_materials.html
│       │   │   ├── service.html
│       │   │   ├── tickets.html
│       │   │   └── contracts.html
│       │   └── static/css/
│       │       ├── dashboard.css
│       │       ├── calendar.css
│       │       ├── work_materials.css
│       │       ├── service.css
│       │       ├── tickets.css
│       │       └── contracts.css
│
│       ├── clientes/
│       │   ├── templates/
│       │   │   ├── dashboard.html
│       │   │   ├── materials.html
│       │   │   ├── contract.html
│       │   │   ├── submission_files.html
│       │   │   └── services.html
│       │   └── static/css/
│       │       ├── dashboard.css
│       │       ├── materials.css
│       │       ├── contract.css
│       │       ├── submission_files.css
│       │       └── services.css
│
│       └── administradores/
│           ├── templates/
│           │   ├── dashboard.html
│           │   ├── view_service.html
│           │   ├── contracts.html
│           │   └── team.html
│           └── static/css/
│               ├── dashboard.css
│               ├── view_service.css
│               ├── contracts.css
│               └── team.css

```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **Jinja2**
- **HTML5 / CSS3**
- **Uvicorn**
- **JWT para autenticação**
- **dotenv para variáveis de ambiente**

---

## 🔐 Backend - Segurança

Arquivo `security.py`:

- `criar_token_jwt(data: dict)`: Gera JWT.
- `verificar_token_jwt(token: str)`: Decodifica e valida token.
- `verificar_cpf(cpf: str)`: Verifica se o CPF já está cadastrado.
- `verificar_usuario_logado(token: str)`: Middleware para checar se o usuário está autenticado.

---

## 👥 Perfis de Usuário

- **Cliente**:
  - Visualiza serviços
  - Acessa calendário e agenda
  - Autenticado por JWT
  - Templates: `calendário.html`, `services.html`, etc.

- **Administrador**:
  - Acessa dashboard de controle
  - Gerencia serviços
  - Templates: `dashboard.html`, `view_service.html`, etc.

---

## 🎨 Frontend - Temas e Layout

Arquivos de tema:

- `theme_light.css`: Tema claro
- `theme_dark.css`: Tema escuro
- `base.css`: Estilos comuns globais
- Alternância via JavaScript (`data-theme` no `html`)

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
