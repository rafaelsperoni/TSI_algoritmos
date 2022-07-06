primeironome = "rafael"
matricula = "202100036"

login = input("Informe o nome do usuario: ")
senha = input("Informe a senha: ")

if login==primeironome and senha==matricula:
    print("Aceso permitido")
else:
    print("Acesso negado")