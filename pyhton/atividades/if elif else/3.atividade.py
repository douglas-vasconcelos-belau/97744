import os

os.system ("clear")

numero1= float (input("digite o primeiro numero:"))
numero2 = float (input("digite o segundo numero:"))
soma = (numero1 + numero2)
media = soma / 2
mult = (numero2 * numero1 )

print ()
print (f"a soma é: {soma}")
print (f"a media é: {media}")
print (f"o produto é: {mult}")

print ()
if numero1 > numero2 :
    print (f"{numero2} é menor que {numero1}")
    
elif numero1 == numero2:
    print (f"{numero1} é igual ao {numero2}")

else:
    print (f"{numero1} é menor que {numero2}")