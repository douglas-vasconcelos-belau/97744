
import os

import time

numero = int (input("degite um numero: "))

print("iniciando contagem: ")
for i in range (numero, 0, -1):
    print (f"numero: {i}")
    time.sleep(1) 

print ("acabou")