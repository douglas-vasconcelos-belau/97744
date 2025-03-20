import os

os.system ("clear")


while True :
    nota1 = float (input("digite sua primeira nota: "))

    if nota1  < 0 or nota1  > 10 :
        print()
        print("nota invalida, tente novamente.\n")
        print()
    else:
        break
while True :
    nota2 = float (input("digite sua segunda nota: "))

    if nota2 < 0 or nota2  > 10 :
        print()
        print("nota invalida, tente novamente.\n")
        print()
    else:
        break

media = (nota1 + nota2) / 2

print (f"sua media é: {media}") 

#outra forma

soma = 0

for i in range (2) :
    while True:
        nota = float(input(f"digite a {i+1} nota:ª "))

        if nota < 0 or nota > 10:
            print("nota invalida< tente novamente./n")
        else:
            soma += nota
            break

media = soma /2

print(f"media: {media}")