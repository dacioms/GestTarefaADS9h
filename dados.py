import csv

# Função para ler o último ID utilizado a partir do arquivo CSV
def ler_ultimo_id(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                ultimo_id = int(linha[0])
    except FileNotFoundError:
        # Se o arquivo não existir, retorna 0 como o último ID
        ultimo_id = 0
    return ultimo_id

# Função para escrever o próximo ID no arquivo CSV
def escrever_proximo_id(nome_arquivo, proximo_id):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([proximo_id])

# Função para ler dados de um arquivo CSV
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)

# Função para escrever dados em um arquivo CSV
def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in dados:
            escritor_csv.writerow(linha)

# Função para remover linha do arquivo CSV com base no ID
def remover_linha_csv(arquivo, id_remover):
    with open(arquivo, 'r', newline='') as arquivo_csv:
        linhas = list(csv.reader(arquivo_csv))

    with open(arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in linhas:
            if linha[0] != id_remover:
                escritor_csv.writerow(linha)

# Capturar dados do usuário
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
cidade = input("Digite a cidade: ")

# Definir o nome do arquivo para armazenar o último ID utilizado
arquivo_ultimo_id = 'ultimo_id.csv'

# Ler o último ID utilizado ou definir como 0 se for a primeira execução
ultimo_id = ler_ultimo_id(arquivo_ultimo_id)

# Gerar o próximo ID único
proximo_id = ultimo_id + 1

# Dados a serem escritos no arquivo CSV
dados_para_escrever = [
    [proximo_id, nome, idade, cidade]
]

# Exemplo de uso
arquivo_saida = 'exemplo.csv'

# Escrever dados no arquivo CSV sem sobrescrever os dados antigos
escrever_csv(arquivo_saida, dados_para_escrever)

# Escrever o próximo ID no arquivo CSV
escrever_proximo_id(arquivo_ultimo_id, proximo_id)

# Ler dados do arquivo CSV
ler_csv(arquivo_saida)

# Remover uma linha com base no ID
id_remover = input("Digite o ID a ser removido: ")
remover_linha_csv(arquivo_saida, id_remover)
