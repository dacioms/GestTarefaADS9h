from tkinter import *
from NovaTarefa import abrir_nova_janela
from Utils import definirTamanhoTela
from tarefa import tarefaDisplay

listaTarefas = [
    {
        "id": 1,
        "nome": "Fazer compras",
        "descricao": "Fazer compras no mercado e comprar manteiga",
        "data": "2024-03-08",
        "concluido": False
    },
    {
        "id": 2,
        "nome": "Estudar",
        "descricao": "Estudar informática",
        "data": "2024-03-12",
        "concluido": True
    },
    {
        "id": 3,
        "nome": "Dormir",
        "descricao": "Dormir muito",
        "data": "2024-03-14",
        "concluido": False
    },
]


mostrarConcluidos = False 
tarefas_nao_concluidas = [tarefa for tarefa in listaTarefas if not tarefa["concluido"]]
tarefas_concluidas = [tarefa for tarefa in listaTarefas if tarefa["concluido"]]

def mudarTarefas():
    global mostrarConcluidos
    mostrarConcluidos = not mostrarConcluidos

    for widget in container.winfo_children():
        widget.destroy()
    
    if (mostrarConcluidos):
        for conteudo in tarefas_nao_concluidas:
            tarefaDisplay(container, conteudo.get("id"), conteudo.get("nome"), conteudo.get("descricao"), conteudo.get("data"), conteudo.get("concluido"))
    else:
        for conteudo in tarefas_concluidas:
            tarefaDisplay(container, conteudo.get("id"), conteudo.get("nome"), conteudo.get("descricao"), conteudo.get("data"), conteudo.get("concluido"))

root = Tk()
root.title("Minhas tarefas")

window = Frame(root)
window.pack(fill=X)

header = Frame(window)
header.pack(fill=X, padx=10, pady=10)

add = Button(header, text="Adicionar tarefa", bg="#6aa84f", bd=0, pady=8, padx=15, fg="white", font=("Arial", 10, "bold"), command=abrir_nova_janela)
add.pack(side=RIGHT, padx=(5, 0))

mostrar = Button(header, text="Mostrar concluídos", bg="#dddddd", bd=0, pady=8, padx=15, fg="#747474", font=("Arial", 10, "bold"), command=mudarTarefas)
mostrar.pack(side=RIGHT)

container = Frame(window)
container.pack(fill=X)

mudarTarefas()


definirTamanhoTela(root)


    
            


root.mainloop()
