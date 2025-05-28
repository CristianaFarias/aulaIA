#Desenvolva uma calculadora que realize as quatro operações básicas (+, -, *, /) entre dois números.
#Solicitar ao usuário dois números e a operação.
#Repetir até que uma operação válida seja concluída.
#Tratar os seguintes erros: Entrada não numérica, divisão por zero, operação inválida.
while True:
    try:
        primeiro = float(input("Digite o primeiro número: "))
        segundo = float(input("Digite o segundo número: "))
        operacao = float(input(("Qual operação gostaria de realizar: 1-Soma, 2-Subtração, 3-Multiplicação ou 4-Divisão? ")))
        if operacao == 1:
            resultado = primeiro + segundo
            print(f"O resultado de {primeiro}+{segundo} = {resultado:.2f}")
            break
        elif operacao == 2:
            resultado = primeiro - segundo
            print(f"O resultado de {primeiro}-{segundo} = {resultado:.2f}")
            break
        elif operacao == 3:
            resultado = primeiro * segundo
            print(f"O resultado de {primeiro}*{segundo} = {resultado:.2f}")
            break
        elif operacao == 4:
            resultado = primeiro / segundo
            print(f"O resultado de {primeiro}/{segundo} = {resultado:.2f}")
            break
    except ValueError:
        print("Você deve digitar um números.")
    except ZeroDivisionError:
        print("Você deve fornecer números maiores que 0.")
    except TypeError:
        print("Operação inválida.")

  
       
    
