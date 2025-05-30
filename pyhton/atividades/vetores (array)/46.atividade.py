import os

os.system ("clear")

lista = []

for i in range (4):
    nota = float(input(f"digite sua {1 + i}º nota : "))
    lista.append(nota)

def medi ():
    media = sum (lista) / 4
    return media
    
medias = medi ()

if medias >= 7:
    print("aprovado")
elif medias >= 5:
    print("recuperaçao")
else:
    print("reprovado")

print()
for nota in lista:
    print(f"nota:{nota}")

print()
print(f"media: {medias}")