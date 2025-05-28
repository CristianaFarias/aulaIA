#Desenvolva uma calculadora que realize as quatro operações básicas (+, -, *, /) entre dois números.
#while True:
#try:
    #primeiro = int(input("Digite o primeiro numero: "))
    # segundo = int(input("Digite o segundo numero: "))
    # operacao = int(input(("Qual operação gostaria de realizar: 1-Soma, 2-Subtração, 3-Multiplicação ou 4-Divisão? ")))
    # if operacao == 1:
        # resultado = primeiro + segundo
        # print(f" O resultado de {primeiro}+{segundo} = {resultado}")
    # elif operacao == 2:
        # resultado = primeiro - segundo
        # print(f" O resultado de {primeiro}-{segundo} = {resultado}")
    # elif operacao == 3:
        # resultado = primeiro * segundo
        # print(f" O resultado de {primeiro}*{segundo} = {resultado}")
    # elif operacao == 4:
        # resultado = primeiro / segundo
        # print(f" O resultado de {primeiro}/{segundo} = {resultado}")
# except ValueError:
    # print("Você deve digitar números.")
# except ZeroDivisionError:
    # print("Você deve fornecer numeros maiores que 0.")
# except TypeError:
    # print("")

while True: 
    try:
        numero1 = float(input("Digite o primeiro número"))
        numero2 = float(input("Digite o primeiro número"))
        operacao = input("Digite a operação ( +, -, *, /)")
        if operacao == "+":
            print("Resultado:", numero1 +  numero2)
            break
        elif operacao == "-":
             print("Resultado:", numero1 -  numero2)
             break
        elif operacao == "*":
             print("Resultado:", numero1 * numero2)
             break
        elif operacao == "-":
             print("Resultado:", numero1 /  numero2)
             if numero2 == 0:
                  print("ERRO! Divisão por zero.")
             else:
                  print("Resualtado:", numero1/numero2)
                  break
    except ValueError:
                  print("operação inválida.")


    
       
    
