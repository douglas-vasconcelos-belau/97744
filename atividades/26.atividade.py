import os

os.system ("clear")

senha_c = "q"
login_c = "q"

while True:
    senha = str (input("digite sua senha: "))
    login = str (input("digite seu usuario: "))

    if senha != senha_c or login != login_c:
        print()
        print("senha ou usuario incorretos")
        print()
    else:
        print()
        print ("acesso permitido")
        break

        
