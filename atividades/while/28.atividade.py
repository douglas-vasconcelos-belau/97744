import os

os.system ("clear")


while True :
    nota1 = float (input("digite sua primeira nota: "))
    nota2 = float (input("digite sua segunda nota: "))
    nota3 = float (input("digite sua terceira nota: "))

    if nota1  < 0 or nota1  > 10 and nota2  < 0 or nota2  > 10 and nota3  < 0 or nota3  > 10 :
        print()
        print("nota invalida, tente novamente.\n")
    else:
        break


media = (nota1 + nota2 + nota3 ) / 3

if media >= 7:
    print(f"parabens voce foi aprovado com media: {media}")
elif media >= 5:
    print(f"voce esta de recuperaçao com media: {media}")
else:
    print(f"voce foi reprovado com media: {media}")



print(f"media:{media:.2f}")