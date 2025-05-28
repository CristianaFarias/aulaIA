#conversor de temperatura
temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").lower()
convertido = input("Unidade de destino C, F ou K: ").lower()
if origem == convertido:
    print(f"A temperatura já está em {temperatura}°{convertido.upper()}")
#origem C
elif origem == "c" and  convertido == "f":
    resultado = (temperatura*9/5)+32
    #print(f"{temperatura:.1f}°C = {resultado:.1f}°F ")
elif origem == "c" and convertido == "k":
    resultado = temperatura + 273.15
    #print(f"{temperatura:.1f}°C = {resultado:.1f}°K ")
#origem F
elif origem == "f" and convertido == "c":
    resultado = (temperatura - 32)*5/9
    #print(f"{temperatura:.1f}°F = {resultado:.1f}°C ")
elif origem =="f" and convertido == "k":
    resultado = (temperatura - 32) * 5/9 + 273.15
    #print(f"{temperatura:.1f}°F = {resultado:.1f}°K ")
#origem K
elif origem == "k" and convertido == "c":
    resultado = temperatura -273.15
    #print(f"{temperatura:.1f}°K = {resultado:.1f}°C ")
elif origem == "k" and convertido == "f":
    resultado = (temperatura - 273.15) * 9/5 + 32
    #print(f"{temperatura:.1f}°K = {resultado:.1f}°F ")
else:
    #print("Tente novamente.")
    resultado = None
if resultado is not None:
    print(f"{temperatura}° = {resultado}°{convertido}")
else:
    print("Use apenas C, K ou F")
