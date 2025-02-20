import os

os.system ("clear")

senha_c = "que"
login_c = "douglas"
login = str (input("digite seu login:"))
senha = str (input("digite sua senha:"))

if login_c ==login and senha_c ==senha :
    print ("bem vindo")
else:
    print("login ou senha invalido")

    