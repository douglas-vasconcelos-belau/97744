import os

os.system ("clear")

lista = []

for i in range (4):
    nota = float(input(f"digite sua {1 + i}º nota : "))
    lista.append(nota)

media = sum (lista) / 4

if media >= 7:
    print("aprovado")
elif media >= 5:
    print("recuperaçao")
else:
    print("reprovado")

print()
for nota in lista:
    print(f"nota:{nota}")

print()
print(f"media: {media}")