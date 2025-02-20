import os

os.system ("clear")

idade=int(input("digite sua idade: "))

if idade >=18 and idade <= 65 :
    print("voto é obrigatorio")
elif idade == 16 or idade == 17:
    print ("voto opicional")
else:
    print("voto nao é obrigatorio")
 