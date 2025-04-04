import os

os.system ("clear")

def med (n1,n2):
    media = (n1 + n2) / 2
    return media

n1 = int (input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))

media = med (n1,n2)

print (f"media do aluno: {media}")
