import csv
import os

arquivo_saida = 'dados.csv'

def ler_csv():
    """
    Lê os dados de um arquivo CSV e retorna uma lista de dicionários representando cada linha do arquivo.

    Returns:
        list: Uma lista de dicionários representando os dados do arquivo CSV.
    """
    lista_objetos = []
    with open(arquivo_saida, newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            lista_objetos.append(linha)
    return lista_objetos

def verificar_arquivo():
    """
    Verifica se o arquivo CSV existe.

    Returns:
        str: Retorna 'a' se o arquivo existe (modo de acrescentar), 'w' se não existe (modo de escrita).
    """
    if os.path.exists(arquivo_saida):
        return 'a'
    else:
        return 'w'

def atribuir_ids_auto_incrementais(dados):
    """
    Atribui IDs automaticamente aos itens da lista, começando a partir do último ID encontrado no arquivo CSV.

    Args:
        dados (list): Uma lista de dicionários representando os dados a serem escritos no arquivo CSV.
    """
    max_id = 0
    dados_csv = ler_csv()
    if dados_csv:
        max_id = max(int(item['id']) for item in dados_csv)
    else:
        max_id = 0

    for item in dados:
        if 'id' not in item:
            max_id += 1
            item['id'] = str(max_id)
   

    

def escrever_csv(dados):
    """
    Escreve os dados em um arquivo CSV.

    Args:
        dados (list): Uma lista de dicionários representando os dados a serem escritos no arquivo CSV.
    """
    modo_escrita = verificar_arquivo()

    with open(arquivo_saida, modo_escrita, newline='') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=dados[0].keys())
        
        atribuir_ids_auto_incrementais(dados)
        if modo_escrita == 'w':
            escritor_csv.writeheader()

        for objeto in dados:
            escritor_csv.writerow(objeto)
    
# TODO fazer funcionar
def remover_elemento_por_id(id_para_remover):
    """
    Remove uma linha do arquivo CSV com base no ID especificado.

    Args:
        id_para_remover (str): O ID do elemento a ser removido.
    """
    linhas = []
    with open(arquivo_saida, 'r', newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            if linha['id'] != id_para_remover:
                linhas.append(linha)

    with open(arquivo_saida, 'w', newline='') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=linhas[0].keys())
        escritor.writeheader()
        escritor.writerows(linhas)
