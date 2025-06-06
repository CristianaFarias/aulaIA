#2- Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​
import  csv 
def escrever_csv(nome_arquivo,dados):
    colunas = ["Nome","Idade","Cidade"]
    with open(nome_arquivo, mode="w", newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo'{nome_arquivo}' criado com sucesso")
dados_pessoa = [
    {"Nome": "Luciana","Idade": 30, "Cidade": "São Bernardo do Campo"},
    {"Nome": "João","Idade": 29, "Cidade": "Ribeirão Preto"},
    {"Nome": "Jonas","Idade": 18, "Cidade": "Iraquara"}
    ]
escrever_csv("alunos.csv",dados_pessoa)