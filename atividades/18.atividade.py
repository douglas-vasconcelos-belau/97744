
pares = 0
impares = 0

for i in range (5):
    numero = int (input("digite um numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print (f"qunatidade de pares: {pares}")
print (f"qunatidade de impares: {impares}")