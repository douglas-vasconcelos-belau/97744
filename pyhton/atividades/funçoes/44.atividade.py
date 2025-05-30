import os

os.system ("clear")

soma = 0

def calculo(soma):
    return soma / 2
    
    
for i in range (2):

    nota = float (input(f"digite o {1+i} numero: "))
    soma +=nota

media = calculo(soma)
print()
print(f"sua media é: {media}")

if media >= 7:
    print("parabens voce foi arpovado")
elif media > 10:
    print("hack")
else:
    print("voce esta reprovado")