from tkinter import *
from NovaTarefa import abrir_nova_janela

def tarefaDisplay(window, id, nome, descricao, data, concluido):

    def abrir_editar():
        abrir_nova_janela(id, nome, descricao, data)

    def deletar():
        # crud.delete(id) 
        print(f"Tarefa {id} deletada")

    def verificar_checkbox():

        if var.get() == 1:
            print("Concluído")
            # crud.update({ "id": id, "nome": nome, "descricao": descricao, "data": data, "concluido": True })
        else:
            print("Não concluído")
            # crud.update({ "id": id, "nome": nome, "descricao": descricao, "data": data, "concluido": False })

    data = data.split("-")[::-1]
    dataFormatada = "/".join(data)

    div = Frame(window, bg="white", pady=10)
    div.pack(fill=X, expand=True, padx=10, pady=10)

    var = IntVar()
    checkbox = Checkbutton(div, bg="white", variable=var, command=verificar_checkbox)
    checkbox.grid(row=0, column=0, rowspan=2, padx=(10, 0))

    nomeTexto = Label(div, bg="white", text=f"{nome}", font=("Arial", 11, "bold"), anchor="w")
    nomeTexto.grid(row=0, column=1, sticky="w", padx=30)

    descricaoTexto = Label(div, bg="white", text=f"{descricao}", font=("Arial", 10, "normal"), anchor="w")
    descricaoTexto.grid(row=1, column=1, sticky="w", padx=30)

    dataTexto = Label(div, bg="white", text=f"{dataFormatada}", font=("Arial", 10, "normal"), anchor="e")
    dataTexto.grid(row=0, column=2, rowspan=2, sticky="e")

    editar = Button(div, text="Editar", bg="#ddcf47", fg="white", font=("Arial", 10, "bold"), command=abrir_editar)
    editar.grid(row=0, column=3, rowspan=2, sticky="e")

    deletar = Button(div, text="X", bg="red", fg="white", font=("Arial", 10, "bold"), command=deletar)
    deletar.grid(row=0, column=4, rowspan=2, sticky="e")

    if (concluido):
        var.set(1)
    else:
        var.set(0)
    

    
        

