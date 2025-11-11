# TaskIO

API simples de TODO

## 🚀 Principais Funcionalidades

- Criação de Tarefas: Adicione novas tarefas com título e descrição.

- Gestão de Status: Marque tarefas como concluídas ou reverta para pendentes.

- Edição Completa: Atualize o título, descrição ou status de qualquer tarefa.

- Remoção de Tarefas: Delete tarefas que não são mais necessárias.

- Listagem e Filtragem:

    - Liste todas as tarefas.

    - Filtre apenas tarefas pendentes.

    - Filtre apenas tarefas concluídas.

- Assíncrono: Todos os endpoints do banco de dados são async/await, garantindo que a API não bloqueie.

- Documentação Automática: Interface Swagger UI e ReDoc gerada automaticamente pelo FastAPI.

## 🛠️ Stack de Tecnologias

- FastAPI: Para a criação da API web de alta performance.

- Pydantic: Para validação de dados de entrada e saída (schemas).

- SQLAlchemy (Async): Para o ORM e comunicação assíncrona com o banco de dados.

- Aiosqlite: Driver de banco de dados assíncrono para SQLite.

- Uvicorn: Como servidor ASGI para rodar a aplicação.

## 📂 Estrutura do Projeto

```

/
├── app/
│   ├── __init__.py
│   ├── app.py       
│   ├── db.py        
│   └── schemas.py   
├── run.py           
└── tasks.db         

```