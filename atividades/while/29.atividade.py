import os

os.system ("clear")


pares = 0
impares = 0
somage = 0
somapa = 0 
quantidadege = 0

while True: 
    num = int (input("digite um numero: (0 para parar)"))
    
    if num == 0:
        break
        
    if num % 2 == 0:
        pares += 1
        somapa += num
    else:
        impares += 1


    somage += num
    quantidadege += 1
    
if quantidadege > 0 :

    mediapa = somapa / pares
    mediage =  somage / quantidadege
    
    print()
    print(f"quantidade de pares: {pares}")
    print(f"quantidade de impares: {impares}")
    print(f"media dos pares: {mediapa}")
    print(f"media geral dos numeros: {mediage}")
else:
    print ("\nnao foram informados os numeros necessarios para a operaçao")

