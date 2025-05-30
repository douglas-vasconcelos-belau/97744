import os

os.system ("clear")

def tabuada(numero):
    for i in range (1,11):
         print (f"{numero} x {i} = {numero * i}")

print("==TABUADA==")
numero = int(input("degite um numero: "))
tabuada (numero)

