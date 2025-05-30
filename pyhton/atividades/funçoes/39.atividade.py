import os

os.system ("clear")


def num():
    contadorpar = 0
    contadorim = 0

    for i in range (6):

        numero = int(input("digite o um numero: "))

        if numero % 2 == 0:
            contadorpar += 1
            
        else:
            contadorim += 1
    return contadorim, contadorpar
    
quantidadepares, quantidadeimpares = num()

print(f"\nquantidade de numeros pare: {quantidadepares}")
print(f"quantidade de numeros impare: {quantidadeimpares}")
        