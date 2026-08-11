from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from lista import ToDoList


class TarefaItem(BaseModel):
    tarefa: str


app = FastAPI(title='Lista de Tarefas API')

todo = ToDoList()


@app.get('/tarefas', response_model=list[str])
def listar_tarefas():
    return todo.listar_tarefas()


@app.post('/tarefas', response_model=str, status_code=201)
def criar_tarefa(item: TarefaItem):
    try:
        return todo.adicionar_tarefa(item.tarefa)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.delete('/tarefas/{numero}', response_model=str)
def deletar_tarefa(numero: int):
    try:
        return todo.remover_tarefa(numero)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=str(error))
