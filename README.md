# Lista de Tarefas

Interface gráfica simples para gerenciar tarefas usando a classe `ToDoList`.

## Arquivos
- `lista.py` — lógica principal (classe ToDoList).
- `gui_tk.py` — interface gráfica com Tkinter.
- `README.md` — este arquivo.

## Requisitos
- Python 3.8+ (Tkinter já vem na instalação padrão do Windows).

## Executar
Abra o terminal na pasta do projeto:
- Rodar a interface gráfica:
  ```
  python gui_tk.py
  ```
- Rodar a versão CLI:
  ```
  python lista.py
  ```

## Uso rápido (GUI)
- Digite a tarefa no campo e clique em "Adicionar Tarefa".
- Selecione uma tarefa na lista e clique em "Remover Selecionada".

## Observações
- Validações básicas estão em `lista.py` (nome obrigatório, índices válidos).