#Calculadora de IMC
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura*altura)
if imc <18.4:
    print(f"IMC: {imc:.1f}\nClassificação: Abaixo do peso.")
elif imc<25:
    print(f"IMC: {imc:.1f}\nClassificação: Peso normal.")
elif imc<30:
    print(f"IMC: {imc:.1f}\nClassificação: Sobrepeso.")
else:
    print(f"IMC: {imc:.1f}\nClassificação: Obeso.")