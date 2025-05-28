# Crie um programa que verifique se a senha é forte.
# Regras:
# Senha forte: pelo menos 8 caracteres e pelo menos um número.
# Continuar pedindo senha até que uma válida seja inserida ou o usuário digite 'sair'.
print("Verificador de senhas.\nRegras:\nA senha deve contar no mínimo 8 caracteres e pelo menos  um numero.")
while  True:
    senha = input("Digite sua senha ou digite 'Sair' para enserrar o programa.\n-> ")
    if senha.lower() == "sair":
        break
    if len(senha) < 8:
            print("Uma senha forte deve ter pelo menos 8 caracteres.")
            continue
    tem_numero = False
    if any(c.isdigit() for c in senha):
             tem_numero = True
    if not tem_numero:
        print("Uma senha forte deve conter pelo menos um número.")
        continue
    print("Senha forte, parabéns")
    break
