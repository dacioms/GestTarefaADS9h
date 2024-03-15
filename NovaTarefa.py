from tkinter import *
from Utils import definirTamanhoTela
from tkcalendar import DateEntry
from locale import setlocale, LC_ALL
import datetime
        
add_janela = None

def abrir_nova_janela(id = -1, nome = "", descricao = "", data = ""):
    setlocale(LC_ALL, 'pt_BR')
    global add_janela

    if add_janela is not None and add_janela.winfo_exists():
        add_janela.lift()
    else:

        print(data)

        def enviar():
            # if (id == -1):
                # crud.create({ "nome": campo_nome.get(), "descricao": campo_descricao.get(), "data": campo_data.get_date(), "concluido": True })
            # else:
                # crud.update({ "id": id, "nome": campo_nome.get(), "descricao": campo_descricao.get(), "data": campo_data.get_date(), "concluido": True })
            
            nova_janela.destroy()

        nova_janela = Toplevel()

        window = Frame(add_janela)
        window.pack(fill=BOTH, expand=True)

        header = Frame(window)
        header.pack(fill=X, expand=True, side=TOP, padx=10, pady=10)

        # Nome da tarefa
        label_nome = Label(nova_janela, text="Nome da Tarefa")
        label_nome.pack(padx=5, pady=(50, 5))
        campo_nome = Entry(nova_janela, width=30)
        campo_nome.insert(END, nome)
        campo_nome.pack(padx=5, pady=5)
        
        # Descrição da tarefa
        label_descricao = Label(nova_janela, text="Descrição da Tarefa")
        label_descricao.pack(padx=10, pady=5)
        campo_descricao = Entry(nova_janela, width=30)
        campo_descricao.insert(END, descricao)
        campo_descricao.pack(padx=5, pady=5)
        
        # Data da tarefa
        label_data = Label(nova_janela, text="Data da Tarefa")
        label_data.pack(padx=10, pady=5)
        campo_data = DateEntry(nova_janela, width=28, background='darkblue', foreground='white', borderwidth=2, locale='pt_BR', date_pattern='dd/mm/yyyy')
        campo_data.pack(padx=5, pady=5)

        # Botão
        btnAddTarefa = Button(nova_janela, text="Enviar", bg="#6aa84f", bd=0, pady=8, padx=15, fg="white", font=("Arial", 10, "bold"), command=enviar)
        btnAddTarefa.pack(pady=10)

        if (id != -1): campo_data.set_date(datetime.date(int(data[2]), int(data[1]), int(data[0])))
        
        definirTamanhoTela(nova_janela, 300, 400)


