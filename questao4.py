nome_produto = input("Nome do produto: ")
preco = float(input("Preço unitario: R$ "))
quantidade = int( input("Quantidade: "))
preco_total = preco * quantidade 
print("Nome do produto: ", nome_produto)
print(f"Preço unitario: R$ {preco:.2f}")
print("Quantidade: ", quantidade)
print(f"Total a pagar: R$ {preco_total:.2f}")
