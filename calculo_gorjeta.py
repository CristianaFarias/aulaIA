#pratica 05:Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.​
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round( gorjeta, 2)

total_compra = 100
porcentagem = 15
gorjeta = calcular_gorjeta(total_compra,porcentagem)
print(f"Para uma conta de R$ {total_compra:.2f}, a gorjeta de {porcentagem}% é igual  R$ {gorjeta:.2f}")