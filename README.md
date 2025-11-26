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
- **Autenticação JWT**: Login com token Bearer JWT
- **Gerenciamento de Usuários**: Obtenha dados do usuário autenticado
- **Gerenciamento de Senhas**: Hashing com Argon2 para segurança

### Características Técnicas
- **Assíncrono**: Todos os endpoints utilizam async/await, evitando bloqueios
- **Validação Robusta**: Pydantic garante dados válidos em requisições
- **Documentação Automática**: Swagger UI e ReDoc disponíveis automaticamente
- **Banco de Dados Automático**: Tabelas criadas automaticamente no startup

## 🛠️ Stack de Tecnologias

- **FastAPI**: Framework web de alta performance com validação automática
- **Pydantic**: Validação de dados, serialização e gerenciamento de configurações
- **SQLAlchemy (Async)**: ORM assíncrono com suporte a múltiplos bancos
- **FastAPI-Users**: Sistema completo de autenticação e autorização
- **Aiosqlite**: Driver SQLite assíncrono
- **Uvicorn**: Servidor ASGI de alta performance
- **Python-dotenv**: Gerenciamento seguro de variáveis de ambiente
- **Argon2-CFI**: Hash de senhas com Argon2

## 📂 Estrutura do Projeto

```
app/
├── __init__.py
├── app.py                 # Aplicação FastAPI com lifespan
├── config.py              # Configuração centralizada (variáveis de ambiente)
├── db.py                  # Configuração do banco de dados SQLAlchemy
├── models.py              # Modelo de dados (Tasks)
├── schemas.py             # Schemas de validação (Pydantic)
├── crud.py                # Operações CRUD de tarefas
├── routers/
│   └── __init__.py
├── tasks/
│   ├── __init__.py
│   ├── models.py          # Modelo de tarefa (Task)
│   ├── schemas.py         # Schemas de tarefa (TaskCreate, TaskRead, TaskUpdate)
│   ├── crud.py            # Operações CRUD de tarefas
│   └── router.py          # Endpoints de tarefas
└── users/
    ├── __init__.py
    ├── models.py          # Modelo de usuário
    ├── schemas.py         # Schemas de usuário (UserRead, UserCreate, UserUpdate)
    ├── manager.py         # Gerenciador de usuários
    ├── auth.py            # Configuração JWT e autenticação
    └── router.py          # Endpoints de autenticação e usuários
main.py                     # Ponto de entrada da aplicação
.env                        # Variáveis de ambiente (não versionado)
.env.example                # Template de variáveis de ambiente
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

### Endpoints Principais

#### Tarefas
- `POST /tasks/` - Criar nova tarefa
- `GET /tasks/` - Listar todas as tarefas
- `GET /tasks/pending` - Listar tarefas pendentes
- `GET /tasks/done` - Listar tarefas concluídas
- `PUT /tasks/update/{task_id}` - Atualizar tarefa
- `POST /tasks/complete/{task_id}` - Marcar como concluída
- `DELETE /tasks/delete/{task_id}` - Deletar tarefa

#### Autenticação
- `POST /auth/register` - Registrar novo usuário
- `POST /auth/jwt/login` - Fazer login com JWT
- `POST /auth/jwt/logout` - Fazer logout
- `GET /users/me` - Obter dados do usuário autenticado
- `PATCH /users/{id}` - Atualizar dados do usuário

## ⚠️ Notas Importantes

- O campo `title` é obrigatório ao criar uma tarefa
- Todos os endpoints de tarefas requerem autenticação JWT
- O banco de dados é criado automaticamente no startup
- Senhas são armazenadas com hash Argon2
- Configure uma `SECRET_KEY` segura no arquivo `.env` para produção
- O arquivo `.env` não é versionado (use `.env.example` como referência)

## 🗺️ Roadmap - Melhorias Futuras

- [ ] **Paginação**: Adicionar paginação aos endpoints de listagem de tarefas
- [ ] **Filtros Avançados**: Filtros por data de criação, prioridade, tags e busca por texto
- [ ] **Testes Automatizados**: Suite de testes unitários e de integração com pytest
- [ ] **Migração para PostgreSQL**: Suporte a banco de dados mais robusto
- [ ] **Docker**: Adicionar Dockerfile e docker-compose para facilitar deployment
- [ ] **Atribuição de Tarefas**: Permitir atribuir tarefas a outros usuários
- [ ] **Categorias/Projetos**: Organizar tarefas em projetos ou categorias
- [ ] **Notificações**: Sistema de notificações para tarefas atribuídas
- [ ] **Rate Limiting**: Implementar rate limiting nos endpoints
- [ ] **Cache**: Adicionar cache de resultados com Redis

## 📝 Licença

MIT
