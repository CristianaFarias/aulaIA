#Calculadora de IMC
peso = float(input("Digite o seu peso KG: "))
altura = float(input("Digite a sua altura M: "))
imc = peso / (altura*altura)
if peso == 0 and altura == 0:
    print(f"Os valores devem ser maior que 0")
elif imc < 18.5:
    print(f"IMC: {imc:.2f}\nClassificação: Abaixo do peso.")
elif imc < 25:
    print(f"IMC: {imc:.2f}\nClassificação: Peso normal.")
elif imc < 30:
    print(f"IMC: {imc:.2f}\nClassificação: Sobrepeso.")
else:
    print(f"IMC: {imc:.2f}\nClassificação: Obeso.") 