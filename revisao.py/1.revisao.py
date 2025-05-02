import os
os.syste('cls || clear')

def calcular_me(lista):
    media = sum (lista) / len(lista)
    return media

lista_nota = []
quantidade_notas = 2

for i in range(quantidade_notas):
    nota = float(input(f"digite a {i+1}ª nota : "))
    lista_nota.append(nota)

media = calcular_me(lista_nota)

print(f"\n Media: {media}")