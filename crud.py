import dados
def create(nome, descricao, data):
    tarefa = [{"nome": nome, "descricao": descricao, "data": data}]
    #dados.escrever_csv(tarefa)


def update (id, nome, descricao, data):
    tarefa = dados.ler_csv(id,nome,descricao,data)
    tarefa['nome']= nome
    tarefa['descricao']= descricao
    tarefa['data']= data
    #dados.escrever_csv(tarefa)
    

#def delete(id):
#verificar com o time 2 como será feita a exclusão
   


