#Atividade 06:
import requests
def gerar_usuario_aleatorio():
    url = 'https://randomuser.me/api/'
    try:
        response = requests.get(url)
        dados = response.json()
        user = dados['results'][0]
        nome = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']
        print("\n nome: {nome}, email: {email}, pais: {pais}")
        print(f"Nome{nome}, email: {email}, país: {pais}")
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
gerar_usuario_aleatorio()