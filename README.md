# Dashboard-Connecta
🇧🇷 PT-BR: Dashboard para agências de marketing de médio e grande porte. Gerencie equipes, clientes e campanhas com métricas em tempo real. Interface responsiva, suporte a temas e integração com MongoDB. Desenvolvido com Python, FastAPI, Jinja2, HTML, CSS e JS.

# 📦 FastAPI Modular Project com MongoDB

Projeto web moderno usando **FastAPI**, **Jinja2**, e **MongoDB** (orientado a documentos). Estrutura modular com foco em separação de responsabilidades, REST APIs, e suporte a papéis de **clientes**, **funcionários** e **administradores**.

---

## 📁 Project Structure



```text
.
├── main.py # Inicialização da aplicação FastAPI
├── .env # Variáveis de ambiente (.env para secrets e URIs)
├── database.py # Conexão MongoDB usando Motor ou Beanie
├── .gitignore
├── README.md

├── backend_api/
│ ├── auth/
│ │ ├── routes.py # /login, /logout, /register
│ │ └── services.py # Hashing, geração de token, login
| | ├── ia/
│ |     ├── routes.py         # Endpoint /ia/ask com POST para requisições ao assistente
│ |     ├── services.py       # Função que usa Langchain com ChatGroq
│ |     └── groq_client.py    # Cliente de conexão com a API da ChatGroq
│ │
│ ├── security/
│ │ └── security.py # JWT, verificação de tokens e CPF
│ │
│ ├── clientes/
│ │ ├── routes.py # /clientes, /clientes/contratos, /clientes/servicos
│ │ ├── services.py # Lógica de negócios dos clientes
│ │ ├── models.py # Documentos Pydantic/Beanie para Cliente, Contrato, Servico
│ │ └── schemas.py # Schemas de entrada/saída
│ │
│ ├── administradores/
│ │ ├── routes.py # /admin/dashboard, /admin/equipe, /admin/contratos
│ │ ├── services.py
│ │ ├── models.py # Documentos Admin, Contratos, Equipe
│ │ └── schemas.py
│ │
│ └── arquivos/
│ ├── routes.py # /upload, /download, /clientes/{id}/anexos
│ ├── services.py # Validação e controle de arquivos
│ └── storage.py # Upload físico (sistema de arquivos ou bucket)

├── frontend_api/
│ ├── auth/
│ │ └── views.py # Templates: login, cadastro, logout
│ │
│ └── fluxos/
│ ├── base.html
│ ├── base.css
│ ├── theme_dark.css
│ ├── theme_light.css
│
│ ├── funcionarios/
│ │ ├── templates/
│ │ │ ├── dashboard.html
│ │ │ ├── calendar.html
│ │ │ ├── work_materials.html
│ │ │ ├── service.html
│ │ │ ├── tickets.html
│ │ │ └── contracts.html
│ │ └── static/css/
│ │ ├── dashboard.css
│ │ ├── calendar.css
│ │ ├── work_materials.css
│ │ ├── service.css
│ │ ├── tickets.css
│ │ └── contracts.css
│
│ ├── clientes/
│ │ ├── templates/
│ │ │ ├── dashboard.html
│ │ │ ├── materials.html
│ │ │ ├── contract.html
│ │ │ ├── submission_files.html
│ │ │ └── services.html
│ │ └── static/css/
│ │ ├── dashboard.css
│ │ ├── materials.css
│ │ ├── contract.css
│ │ ├── submission_files.css
│ │ └── services.css
│
│ └── administradores/
│ ├── templates/
│ │ ├── dashboard.html
│ │ ├── view_service.html
│ │ ├── contracts.html
│ │ └── team.html
│ └── static/css/
│ ├── dashboard.css
│ ├── view_service.css
│ ├── contracts.css
│ └── team.css
```

---

## 🧾 Organização REST com MongoDB

### ✅ **Collections MongoDB**
- `users`: clientes, funcionários, admins diferenciados por tipo
- `services`: solicitações de serviço
- `contracts`: documentos de contrato com status
- `attachments`: arquivos enviados
- `teams`: para gerenciamento interno da equipe admin

---

## 🛠 Tecnologias

- **FastAPI**: Web framework assíncrono
- **MongoDB**: Banco de dados NoSQL
- **Motor** ou **Beanie**: ODM para MongoDB
- **Jinja2**: Templates HTML
- **CSS**: Temas dark/light
- **JWT**: Autenticação com segurança
- **Pydantic**: Validação de dados

---

## 🔐 Padrões REST Aplicados

| Método | Rota                          | Descrição                         |
|--------|-------------------------------|-----------------------------------|
| GET    | `/clientes/{id}`              | Obter dados do cliente            |
| POST   | `/clientes/servicos`          | Enviar solicitação de serviço     |
| GET    | `/clientes/contratos`         | Listar contratos                  |
| POST   | `/clientes/anexos`            | Enviar arquivos                   |
| GET    | `/admin/usuarios`             | Listar usuários                   |
| POST   | `/admin/contratos`            | Criar novo contrato               |
| GET    | `/admin/equipe`               | Gerenciar membros da equipe       |

---

## 📆 Checklist de Desenvolvimento

### Semana 1 – Setup & Estrutura
- [x] Setup do projeto com FastAPI, Jinja2, MongoDB
- [ ] Estrutura de pastas backend/frontend
- [ ] Rotas de autenticação (login, logout, cadastro)
- [ ] Templates de login/cadastro com Jinja2
- [ ] Temas CSS: `base.css`, `theme_light.css`, `theme_dark.css`

### Semana 2 – Clientes e Funcionários
- [ ] Rotas e modelos para `/clientes`
- [ ] Rotas `/clientes/servicos` e `/clientes/contratos`
- [ ] Templates: `dashboard.html`, `submission_files.html`
- [ ] Estilizar páginas do cliente

### Semana 3 – Admin e Arquivos
- [ ] Rotas `/admin/usuarios`, `/admin/equipe`, `/admin/contratos`
- [ ] Upload/download de arquivos
- [ ] Templates admin: `dashboard`, `team`, `view_service`
- [ ] Integração back e front

### Semana 4 – Testes e Entrega
- [ ] Testes automatizados no backend
- [ ] Ajustes finais no frontend
- [ ] Docker/local deploy
- [ ] Revisão e documentação final

