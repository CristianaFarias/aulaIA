#Atividade 06:
import requests
def consulta_cep (cep:str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        dados = response.json()
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


cep = input("Digite o cep da cidade: ").strip()
consulta_cep(cep)    