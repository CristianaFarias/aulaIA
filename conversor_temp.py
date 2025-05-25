#conversor de temperatura
temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").lower()
destino = input("Unidade de destino C, F ou K: ").lower()
if origem == destino:
    print(f"A temperatura já está em {temperatura}°{destino.upper()}")
#origem C
elif origem == "c" and destino == "f":
    resultado = (temperatura*9/5)+32
    print(f"{temperatura:.1f}°C = {resultado:.1f}°F ")
elif origem == "c" and destino == "k":
    resultado = temperatura + 273.15
    print(f"{temperatura:.1f}°C = {resultado:.1f}°K ")
#origem F
elif origem == "f" and destino == "c":
    resultado = (temperatura - 32)*5/9
    print(f"{temperatura:.1f}°F = {resultado:.1f}°C ")
elif origem =="f" and destino == "k":
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"{temperatura:.1f}°F = {resultado:.1f}°K ")
#origem K
elif origem == "k" and destino == "c":
    resultado = temperatura -273.15
    print(f"{temperatura:.1f}°K = {resultado:.1f}°C ")
elif origem == "k" and destino == "f":
    resultado = F = (temperatura - 273.15) * 9/5 + 32
    print(f"{temperatura:.1f}°K = {resultado:.1f}°F ")
else:
    print("Tente novamente.")

