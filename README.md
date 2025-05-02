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
│   │   ├── routes.py            # Rotas de login, logout, cadastro
│   │   └── services.py          # Lógica de autenticação
│   │
│   ├── security/
│   │   └── security.py          # JWT, verificação de usuário/CPF
│   │
│   ├── clientes/
│   │   ├── routes.py            # Rotas REST (GET /clientes, POST /clientes/agendar, etc.)
│   │   └── services.py          # Regras de negócio para clientes
│   │
│   └── administradores/
│       ├── routes.py            # Rotas REST (GET /admin/dashboard, etc.)
│       └── services.py          # Regras de negócio para admins

├── frontend_api/
│   ├── auth/
│   │   └── views.py             # Templates Jinja2: login, cadastro, logout
│   │
│   └── fluxos/
│       ├── base.html
│       ├── base.css
│       ├── theme_dark.css
│       ├── theme_light.css
│
│       ├── clientes/
│       │   ├── templates/
│       │   │   ├── calendario.html
│       │   │   └── services.html
│       │   └── static/css/
│       │       ├── calendario.css
│       │       └── services.css
│
│       └── administradores/
│           ├── templates/
│           │   ├── dashboard.html
│           │   └── view_service.html
│           └── static/css/
│               ├── dashboard.css
│               └── view_service.css
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
