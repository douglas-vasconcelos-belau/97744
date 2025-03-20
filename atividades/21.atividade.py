import os

os.system ("clear")

#exemplo de laço de rapetiçao while.
idade = int(input("digite sua idade:"))

while idade < 18:
    print ("nao autorizado. \nsomente maiores de 18.\n")
    idade = int(input("digite sua idade:"))

print()
print ("acesso permitido.")
print ("fim")