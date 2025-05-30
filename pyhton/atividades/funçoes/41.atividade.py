import os

os.system ("clear")

preco = float(input("digite o preço do produto: "))

def calcular():
    if preco < 100:
        inflacao = preco * 1.1
    else:
        inflacao = preco * 1.2
    return inflacao

inflacao = calcular()

print(f"o preço com as taxas é: {inflacao}")