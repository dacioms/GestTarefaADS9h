from dados import ler_csv, escrever_csv, remover_elemento_por_id

def create(nome, descricao, data, concluido):
    tarefa = [{'nome': nome, 'descricao': descricao, 'data': data, 'concluido': concluido}] # cria uma lista de dicionários
    escrever_csv(tarefa) # escreve uma lista de dicionários


def update (id, nome, descricao, data, conteudo):
    tarefa = ler_csv()[id]
    tarefa['nome'] = nome
    tarefa['descricao'] = descricao
    tarefa['data'] = data
    tarefa['conteudo'] = conteudo
    
    
def delete(id):
    remover_elemento_por_id(id)

def listar():
    tarefas = ler_csv()
    for tarefa in tarefas:
        print(tarefa)