# 4- Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.​

import json 

dados = [{"name": "Juliano","idade": 18,"cidade": "Bela Vista"},
        {"name": "Juliana","idade": 24,"cidade": "São Bernardo do Campo"},
        {"name": "Juliano","idade": 18,"cidade": "Bela Vista"}   ]
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)