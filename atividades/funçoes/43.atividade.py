import os

os.system ("clear")

soma = 0

def calculo(soma):
    return soma / 3
    
    
for i in range (3):

    nota = float (input(f"digite o {1+i} numero: "))
    soma +=nota

media = calculo(soma)
print(f"sua media é: {media}")

