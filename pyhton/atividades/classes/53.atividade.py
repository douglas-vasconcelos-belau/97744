import os
from dataclasses import dataclass
os.system ("clear")


nome1 = str (input("digite o nome da 1ª pessoa: "))
nome2 = str (input("digite o nome da 2ª pessoa: "))
idade1 = int (input("digite a idade da 1ª pessoa: "))
idade2 = int (input("digite a idade da 2ª pessoa: "))

@dataclass
class Endereco:
    # variavel = atributo
    logradouro: str
    numero:int
    cidade: str   

@dataclass 
class pessoa:
    nome: str
    idade: int
    email: str    
    endereco: Endereco


    # funcao = metodo
    def exibir_dados(self):
        print(f"nome: {self.nome}"),
        print(f"idade: {self.idade}"),
        print(f"endereço: {self.endereco.logradouro}, numero: {self. endereco.numero}")

Endereco1 = Endereco(input("digite seu Endereço: "))
pessoa1 = pessoa (nome1,idade1, Endereco1)
pessoa1.exibir_dados()

print()
Endereco2 = Endereco(input("digite seu ENdereço: "))
pessoa2 = pessoa (nome2, idade2, Endereco2)
pessoa2.exibir_dados()
