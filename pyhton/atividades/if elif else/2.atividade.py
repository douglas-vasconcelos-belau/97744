import os

os.system ("clear")

nota1=float (input("digite sua primeira nota:"))
nota2=float (input("digite sua segunda nota:"))
nota3=float (input("digite sua terceira nota:"))
soma = (nota1 + nota2+ nota3)
media = soma / 3

print (f"media: {media}")

if media < 7 :
    print ("reprovado")
elif media==7:
    print("aprovado")
else:
    print ("aprovado")