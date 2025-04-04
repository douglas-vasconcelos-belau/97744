import os

os.system ("clear")

metros = float(input("quantos metros? "))

def reduçao(metros):
     return metros * 100

centimetros = reduçao(metros)

print (f"a quantidade de {metros} metros são equivalentes a {centimetros} centimetros")
