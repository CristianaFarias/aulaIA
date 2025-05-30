#atividade 05: Crie uma função que verifique se uma palavra ou frase é um palíndromo
def verifica_palindromo(palavra):

    palavra = input("Digite a palavra: ").lower()
    palavra_reverso = palavra[::-1]
    if palavra == palavra_reverso:
        print("Sim")
    else:
        print("Não")
verifica_palindromo("")