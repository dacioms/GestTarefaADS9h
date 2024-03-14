from datetime import datetime  
def criarTarefa(tarefas):
    nome = receberNomeTarefa()
    conteudo = receberConteudo(nome)
    data = receberDataTermino(nome)
    #realizar o append numa lista passando nome, conteudo e data como parametro

def receberNomeTarefa():
    while True:
        try:
            nome = input('Informe o nome da tarefa')
            return nome
        except ValueError:
            print('Erro, tente novamente')

def receberConteudo(nome):
    while True:
        try:
            conteudo = input(f'Informe o conteúdo da terefa {nome}: ')
            return conteudo
        except ValueError:
            print('Erro, tente novamente')

def receberDataTermino(nome):
    while True:
            data_termino = input('Informe a data de término da terefa (dia-mês-ano): ')
            if isDateValid (data_termino):
                return data_termino
            print('Erro, tente novamente!')

def isDateValid(data_termino):
    try:
        data = datetime.strptime(data_termino, '%d-%m-%Y')
        return True
    except ValueError:
        return False



 

