#classificador de idade
#Crianca
#Adolescente (13-17)
#Adulto (18-59)
#Idoso (60 anos ou mais )

idade = int(input("Digite sua idade: "))
if idade>=0 and idade<=12:
    print("Classificação: Criança")
elif idade>12 and idade<=17:
    print("Classificação: Adolescente")
elif idade>17 and idade<=59:
    print("Classificação: Adulto")
elif idade>=60:
    print("Classificação: Idoso")
else:
    print("Insira um número válido.")