import os

os.system ("clear")

numero1= int (input("digite o primeiro numero:"))
numero2 = int (input("digite o segundo numero:"))
numero3 = int (input("digite o terceiro numero:"))

maior_numero = max (numero1,numero2,numero3)
menor_numero = min (numero1,numero2,numero3)
print ()
print(f"entre os numeros {numero1},{numero2} e {numero3}")
print (f"o numero maior é: {maior_numero}")
print (f"o numero menor é: {menor_numero}")