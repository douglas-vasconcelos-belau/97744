import os
from dataclasses import dataclass
os.system ("clear")
  
@dataclass 
class Cliente:
    nome: str
    email: str    
    telefone: str

lista_clientes = []
quantidade_clientes = 2

print("informe os dados.")
for i in range (quantidade_clientes): 
    cliente = Cliente(
         nome = (input("digite seu nome : ")),
         email = (input("digite seu email : ")),
         telefone = (input("digite seu telefone : "))
    )
    lista_clientes.append(cliente)
    print()

print("\n== exibir dados ==")
for cliente in lista_clientes:
    print(f"nome: {cliente.nome}")
    print(f"email: {cliente.email}")
    print(f"telefone: {cliente.telefone}")
    print()

    print("== salvando dados dos clientes ==")
    # salvando os dados em txt
    nome_arquivo = "dados_clientes.txt"

    # w = escrita\salvar\sobreescrever
    # a = escrita\ salvar\acumular
    with open(nome_arquivo, "w") as arquivo:
      for cliente in lista_clientes:  
        arquivo.write(F"{cliente.nome},{cliente.email}, {cliente.telefone}\n")

    print("dados salvos com sucesso!")