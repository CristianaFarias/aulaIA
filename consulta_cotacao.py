#Atividade 06: Consulta a cotação atual de uma moeda
import requests
def consulta_cotacao(moeda_origem: str, moeda_destino: str = "BRL"):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    try:
        response = requests.get(url)
        dados = response.json()
        chave = moeda_origem.upper() + moeda_destino.upper()

        if chave in dados:
            cotacao = float(dados [chave]['bid'])
            print(f"Cotação atual de {moeda_origem.upper()} para {moeda_destino.upper()}: R$ {cotacao:.2f}")
        else:
            print(f"Codigo inválido. ")
    except Exception as e:
        print(f"Erro ao consultar: {e}")
moeda = input("Digita a sigla da moeda a ser convertida (ex: USD, EUR, BTC):").strip().upper()
consulta_cotacao(moeda)
