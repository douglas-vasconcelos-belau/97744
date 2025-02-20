import os

os.system ("clear")

idade=int(input("digite sua idade: "))

if idade <18 or idade >65:
    print("voce é obrigrado a votar")
else:
    print("voce nao é obrigrado a votar")