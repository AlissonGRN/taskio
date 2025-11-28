# TaskIO

[🇬🇧 English](README.en.md) | 🇧🇷 Português

API RESTful assíncrona para gerenciamento de tarefas com autenticação JWT e controle de acesso.

## 📋 Descrição

TaskIO é uma aplicação backend desenvolvida com **FastAPI** que oferece gerenciamento completo de tarefas, autenticação de usuários com JWT, paginação e testes automatizados. O projeto demonstra boas práticas de desenvolvimento moderno em Python.

**Acesse:** [Swagger UI](http://localhost:8000/docs) • [ReDoc](http://localhost:8000/redoc)

---

## ✨ Destaques do Projeto

- ✅ **Autenticação JWT**: Sistema seguro com Argon2 para hash de senhas
- ✅ **Controle de Acesso**: Cada usuário gerencia apenas suas tarefas
- ✅ **Paginação**: Listagem com page/size e metadata completa
- ✅ **Testes Automatizados**: Suite com pytest e pytest-asyncio
- ✅ **Banco Assíncrono**: SQLAlchemy async pronto para produção
- ✅ **Configuração Segura**: Variáveis de ambiente com Pydantic Settings

---

## 🚀 Funcionalidades

### Gerenciamento de Tarefas
- Criar, listar, atualizar e deletar tarefas
- Filtrar por status (pendentes/concluídas)
- Paginação com page/size
- Timestamps de criação e conclusão
- Controle de acesso por usuário

### Autenticação e Usuários
- Registro com validação de email
- Login com JWT (1 hora de expiração)
- Visualizar e atualizar perfil
- Senhas com Argon2-CFI

---

## 🛠️ Tecnologias

- **FastAPI** - Framework web de alta performance
- **Pydantic v2** - Validação e configuração
- **SQLAlchemy (Async)** - ORM assíncrono
- **Aiosqlite** - Driver SQLite assíncrono
- **FastAPI-Users** - Autenticação e gerenciamento de usuários
- **Argon2-CFI** - Hash de senhas
- **pytest** - Testes automatizados
- **Uvicorn** - Servidor ASGI

---

## 📂 Estrutura do Projeto

O projeto segue uma arquitetura em camadas com separação clara de responsabilidades:

- **app/**: Aplicação principal com módulos de tarefas e autenticação
- **tests/**: Suite de testes automatizados com pytest
- **main.py**: Ponto de entrada da aplicação
- **.env-exemple**: Template de configuração
- **requirements.txt**: Dependências do projeto

---

## 🔧 Instalação e Setup

### Pré-requisitos
- Python 3.11+
- pip

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/AlissonGRN/taskio.git
cd taskio
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env-exemple .env
# Edite .env com SECRET_KEY e DATABASE_URL
```

5. Execute a aplicação:
```bash
python main.py
```

A API estará disponível em `http://localhost:8000`

---

## 📚 Endpoints

### Autenticação (Público)
- `POST /auth/register` - Registrar novo usuário
- `POST /auth/jwt/login` - Fazer login (retorna JWT)
- `POST /auth/jwt/logout` - Fazer logout

### Tarefas (Requer autenticação)
- `POST /tasks/` - Criar tarefa
- `GET /tasks/` - Listar com paginação
- `GET /tasks/pending` - Listar pendentes
- `GET /tasks/done` - Listar concluídas
- `PUT /tasks/update/{id}` - Atualizar
- `POST /tasks/complete/{id}` - Marcar concluída
- `DELETE /tasks/delete/{id}` - Deletar

### Usuário (Requer autenticação)
- `GET /users/me` - Obter dados do usuário
- `PATCH /users/{id}` - Atualizar usuário

---

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Com output verboso
pytest -v

# Com cobertura
pytest --cov=app tests/
```

Os testes utilizam banco de dados em memória para isolamento.

---

## 📊 Roadmap

- ✅ Autenticação JWT
- ✅ CRUD de tarefas com controle de acesso
- ✅ Paginação
- ✅ Testes automatizados
- ✅ Configuração com .env
- 📋 Migração para PostgreSQL
- 🐳 Docker + docker-compose
- 🔄 Refresh tokens
- 📧 Notificações por email
- 🏷️ Tags/Categorias
- 🚦 Rate limiting

---

Feito com ❤️ por Alisson Nascimento

