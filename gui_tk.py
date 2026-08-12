from lista import ToDoList
from tkinter import messagebox
import tkinter as tk

tdl = ToDoList()

def atualizar_lista():
    lb.delete(0, tk.END)
    for tarefa in tdl.listar_tarefas():
        lb.insert(tk.END, tarefa)


def adicionar_tarefa():
    tarefa = entry.get().strip()
    try:
        tdl.adicionar_tarefa(tarefa)
    except ValueError as error:
        messagebox.showerror('Erro', str(error))
        return
    entry.delete(0, tk.END)
    atualizar_lista()


def remover_tarefa():
    selecao = lb.curselection()
    if not selecao:
        messagebox.showwarning('Aviso', 'Selecione uma tarefa para remover.')
        return
    indice= selecao[0]
    try:
        tarefa_removida = tdl.remover_tarefa(indice + 1)
    except IndexError as error:
        messagebox.showerror('Erro', str(error))
        return
    messagebox.showinfo('Removido', f'Tarefa "{tarefa_removida}" foi removida')
    atualizar_lista()


root = tk.Tk()
root.title('Lista de Tarefas')

frame = tk.Frame(root, padx = 10, pady = 10)
frame.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(frame, width= 40)
entry.grid(row=0, column=0, padx=(0,8), pady=8)
tk.Button(frame, text='Adicionar Tarefa', command=adicionar_tarefa).grid(row=0, column=1)

lb=tk.Listbox(frame, width=50, height=12)
lb.grid(row=1, column=0, columnspan=2, pady=8)

tk.Button(frame, text='Remover Selecionada', command=remover_tarefa).grid(row=2, column=0, columnspan=2)

atualizar_lista()
root.mainloop()