#Atividade 06:
import random
import string
def gerar_senha(tamanho:int) -> str:
    caracters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracters) for _ in range(tamanho))
tamanho = int(input("Digite o tamanho da senha: "))
print("Senha gerada: ",gerar_senha(tamanho))
