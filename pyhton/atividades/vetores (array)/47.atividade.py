import os

os.system ("clear")

lista = []
quantidade = 3

print("===== lista de compras =====")

for i in range (quantidade):
    item = (input(f"digite sua {1 + i}º nota : "))
    lista.append(item)

print("===== lista de itens =====")
for i, item in enumerate (lista,start=1): 
    print(f"{i}º item: {item}")