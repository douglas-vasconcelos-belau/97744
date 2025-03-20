import os

os.system ("clear")


while True:
    idade = int(input("digite sua idade:"))

    if idade < 18 :
        print("nao outorizado.\nsomente maiores de 18.\n")
    else:
        break

print()
print ("acesso permitido.")
print ("fim")