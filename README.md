# Lista de Tarefas

Aplicação simples de lista de tarefas com interface de linha de comando e API REST.

Funcionalidades:

- Adicionar tarefas pelo CLI ou pela API
- Listar tarefas cadastradas
- Remover tarefas pelo número de ordem
- API em FastAPI com endpoints para listar, criar e deletar tarefas

Arquivos principais:

- `lista.py`: lógica da lista de tarefas e interface CLI
- `api.py`: API REST usando FastAPI
- `requirements.txt`: dependências do projeto

Como usar:

1. Executar a interface de linha de comando:
   ```bash
   python lista.py
   ```
2. Executar a API:
   ```bash
   uvicorn api:app --reload
   ```
3. Acessar os endpoints:
   - `GET /tarefas`
   - `POST /tarefas`
   - `DELETE /tarefas/{numero}`

