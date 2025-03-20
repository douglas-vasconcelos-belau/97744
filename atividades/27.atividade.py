import os

os.system ("clear")

senha_c = "q"
login_c = "q"

for i in range (3) :
        senha = str (input("digite sua senha: "))
        login = str (input("digite seu usuario: "))
    
        if login_c == login and senha_c == senha:
            print("acesso permitido")
            break
        else:
            print("acesso negado")
            print (f"numero de tentativa {i}")
        if i == 2:
            print("numero de tentativas excedido")
            
        

print("fim")

# foma com while

senha_c = "q"
login_c = "q"
contador = 0

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
        contador +=1
        break
    if contador == 3:
         print ("numero de tentativas excedidas")
