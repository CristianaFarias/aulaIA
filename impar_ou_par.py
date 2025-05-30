#Crie um programa que solicite números inteiros ao usuário.
#Regras:
#Continuar pedindo números até que o usuário digite 'fim'.
#Informar se o número é par ou ímpar.
#Se não for um número inteiro, informar o erro e continuar
#Ao final, mostrar a quantidade total de números pares e ímpares inseridos.
def classificar_impar_par():
    while True:
        try:   
            numero =(input("Digite um número inteiro,(ou digite Fim.) "))  
            if numero.lower() == "fim":
                break
            else:
                numero = int(numero)
                if numero % 2 == 0:
                    #print(f"O número {numero} é par.")
                    return "É par."
                else:
                    #print(f"O número {numero} é impar.")
                    return "É impar"
        except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
print(classificar_impar_par())