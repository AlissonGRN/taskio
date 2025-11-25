# TaskIO

API RESTful de gerenciamento de tarefas com autenticação de usuários.

## 🚀 Principais Funcionalidades

### Gerenciamento de Tarefas
- **Criação de Tarefas**: Adicione novas tarefas com título (obrigatório) e descrição.
- **Listagem e Filtragem**: 
  - Liste todas as tarefas
  - Filtre apenas tarefas pendentes
  - Filtre apenas tarefas concluídas
- **Gestão de Status**: Marque tarefas como concluídas
- **Atualização**: Atualize título, descrição ou status de qualquer tarefa
- **Remoção**: Delete tarefas que não são mais necessárias

### Autenticação e Usuários
- **Registro de Usuários**: Crie novas contas com validação de email
- **Autenticação JWT**: Login com token Bearer JWT (validade: 1 hora)
- **Gerenciamento de Usuários**: Obtenha dados do usuário autenticado

### Características Técnicas
- **Assíncrono**: Todos os endpoints utilizam async/await, evitando bloqueios
- **Validação Robusta**: Pydantic garante dados válidos em requisições
- **Documentação Automática**: Swagger UI e ReDoc disponíveis automaticamente
- **Banco de Dados Automático**: Tabelas criadas automaticamente no startup

## 🛠️ Stack de Tecnologias

- **FastAPI**: Framework web de alta performance
- **Pydantic**: Validação de dados e serialização
- **SQLAlchemy (Async)**: ORM assíncrono
- **FastAPI-Users**: Sistema de autenticação e gerenciamento de usuários
- **Aiosqlite**: Driver SQLite assíncrono
- **Uvicorn**: Servidor ASGI

## 📂 Estrutura do Projeto

```
app/
├── app.py                 # Aplicação FastAPI com lifespan
├── db.py                  # Configuração do banco de dados
├── models.py              # Modelo de dados (Tasks)
├── schemas.py             # Schemas de validação (Pydantic)
├── crud.py                # Operações de banco de dados (CRUD)
├── routers/
│   ├── __init__.py
│   └── tasks.py           # Endpoints de tarefas
├── tasks/
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── router.py
└── users/
    ├── models.py          # Modelo de usuário
    ├── schemas.py         # Schemas de usuário
    ├── manager.py         # Gerenciador de usuários
    ├── auth.py            # Configuração JWT
    └── router.py          # Endpoints de autenticação
main.py                     # Ponto de entrada
tasks.db                    # Banco de dados SQLite (auto-criado)
```

## 🔧 Instalação e Setup

### Pré-requisitos
- Python 3.11+
- pip ou poetry

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/AlissonGRN/taskio.git
cd taskio
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python main.py
```

A API estará disponível em `http://localhost:8000`

## 📚 Uso da API

### Documentação Interativa
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints Principais

#### Tarefas
- `POST /tasks/` - Criar nova tarefa
- `GET /tasks/` - Listar todas as tarefas
- `GET /tasks/pending` - Listar tarefas pendentes
- `GET /tasks/done` - Listar tarefas concluídas
- `PUT /tasks/update/{task_id}` - Atualizar tarefa
- `POST /tasks/complete/{task_id}` - Marcar como concluída
- `DELETE /tasks/delete/{task_id}` - Deletar tarefa

#### Autenticação (quando implementado)
- `POST /auth/register` - Registrar novo usuário
- `POST /auth/jwt/login` - Fazer login
- `GET /auth/me` - Obter dados do usuário autenticado

### Exemplo de Requisição

Criar uma tarefa:
```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Minha tarefa", "description": "Descrição da tarefa"}'
```

Listar tarefas:
```bash
curl -X GET "http://localhost:8000/tasks/"
```

## ⚠️ Notas Importantes

- O campo `title` é **obrigatório** ao criar uma tarefa
- Todas as operações de banco de dados são assíncronas
- O banco de dados é criado automaticamente no primeiro startup
- O token JWT é válido por 1 hora
- Altere a `SECRET` em `app/users/auth.py` para uma chave segura em produção

## 📝 Licença

MIT
