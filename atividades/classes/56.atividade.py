import os
from dataclasses import dataclass
import time
os.system ("clear")
  
quantidade = 2

@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: float

for i in range (quantidade):
    print()
    carros = Carro(
        marca = (input("digite a marquinha do carro: ")),
        modelo = (input("digite o modelo do carro: ")),
        categoria = (input("digite a categoria do carro: ")),
        preco = (input("digite o preço do carro: "))
    )   
    nome_arquivo = "dados_carros.txt"

    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(F"{carros.marca},{carros.modelo}, {carros.categoria}, {carros.preco}\n")

print()
print("== salvando dados dos carros ==")

time.sleep(3)
    
print()
print("== dados salvos com sucesso! ==")

