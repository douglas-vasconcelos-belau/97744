import os

os.system ("clear")

def num(numero):
    if numero % 2 == 0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é impar")
        
numero = int(input("digite um numero: "))
num(numero)

