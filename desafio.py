from tkinter import *
from NovaTarefa import abrir_nova_janela

class MinhasTarefasApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Minhas Tarefas")

        self.header = Frame(self.master)
        self.header.pack(fill=X, expand=True, side=TOP, padx=10, pady=10) 


