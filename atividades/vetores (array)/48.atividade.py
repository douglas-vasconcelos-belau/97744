import os

os.system ("clear")

lista = []
quantidade = 5

for i in range (quantidade):
    numero = float(input(f"digite o {1 + i}º numero : "))
    lista.append(numero)

def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

maior, menor = maior_menor(lista)

print()
print(f"o maior numero é {maior}")
print(f"o menor numero é {menor}")
