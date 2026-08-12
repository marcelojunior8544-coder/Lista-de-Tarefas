# Lista de Tarefas

Aplicação simples de lista de tarefas com interface de linha de comando, interface gráfica (Tkinter) e API REST.

Funcionalidades:

- Adicionar tarefas pelo CLI, pela GUI ou pela API
- Listar tarefas cadastradas
- Remover tarefas pelo número de ordem (CLI/API) ou selecionando na GUI
- API em FastAPI com endpoints para listar, criar e deletar tarefas

Arquivos principais:

- `lista.py`: lógica da lista de tarefas e interface CLI (classe ToDoList)
- `api.py`: API REST usando FastAPI
- `gui_tk.py`: interface gráfica com Tkinter
- `requirements.txt`: dependências do projeto

Requisitos:
- Python 3.8+ (Tkinter já vem na instalação padrão do Windows)

Como usar:

1. Executar a interface de linha de comando:
   ```bash
   python lista.py
   ```
2. Executar a interface gráfica (Tkinter):
   ```bash
   python gui_tk.py
   ```
3. Executar a API:
   ```bash
   uvicorn api:app --reload
   ```
4. Acessar os endpoints:
   - `GET /tarefas`
   - `POST /tarefas`
   - `DELETE /tarefas/{numero}`

Uso rápido (GUI):
- Digite a tarefa no campo e clique em "Adicionar Tarefa".
- Selecione uma tarefa na lista e clique em "Remover Selecionada".

Observações:
- Validações básicas estão em `lista.py` (nome obrigatório, índices válidos).

