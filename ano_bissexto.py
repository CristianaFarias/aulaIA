#Verificador de ano Bissexto
ano =  int(input("Digite uma data no formato AAAA:"))
if ano%4 != 0:
    print("Não é um ano bissexto.")
elif ano%100 == 0:
    if ano%400 == 0:
        print("É um ano bissexto.")
    else:
        print("Não é um ano bissexto.")
else: 
    print("É um ano bissexto.")