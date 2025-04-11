import os

os.system ("clear")

listanume = []
listaim= []
listapar= []
quantidade = 6

def num():

    for i in range (6):

        numero = int(input("digite o um numero: "))
        
        listanume.append(numero)
        
        if numero % 2 == 0:
            listapar.append(numero)
        else:
            listaim.append(numero)
    return listapar, listaim, listanume

    
listapar, listaim, listanume = num()

print(f"\nnumeros digitados: {listanume}")
print(f"\nnumeros pares: {listapar}")
print(f"numeros impare: {listaim}")
