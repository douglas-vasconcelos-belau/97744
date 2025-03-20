import os

os.system ("clear")


while True :
    nota = float (input("digite sua nota: "))

    if nota >= 0 or nota <= 10 :
        print("nota invalida, tente novamente.\n")
    else:
        break
    
print (f"sua nota é: {nota}") 