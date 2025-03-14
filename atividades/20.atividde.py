import os

os.system ("clear")

soma = 0

for i in range (3):
    nota = int(input("digite um sua nota: "))
    soma += nota

media = soma / 3

if media >= 7:
    print(f"parabens voce foi aprovado com media: {media}")
elif media <7 or 4 :
    print(f"voce esta de recuperaçao com media: {media}")
else:
    print(f"voce foi reprovado com media: {media}")

    