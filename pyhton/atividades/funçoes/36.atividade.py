import os

os.system ("clear")

def num(numero):
    if numero > 0 :
        print(f"o numero {numero} é positivo")
    elif numero == 0:
        print(f"o numero {numero} é neutro")
    else:
        print(f"o numero {numero} é negativo")
        
numero = int(input("digite um numero: "))
num(numero)