import os
from dataclasses import dataclass


@dataclass
class Endereco:
    # variavel = atributo
    logradouro: str
    numero:int
    
@dataclass 
class pessoa:
    nome: str
    idade: int
    endereco: Endereco

    # funcao = metodo
    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"endereço: {self.endereco.logradouro}, numero: {self. endereco.numero}")

Endereco1 = Endereco("Rua A", 23)
pessoa1 = pessoa ("marta", 44, Endereco1)
pessoa1.exibir_dados()

print()
Endereco2 = Endereco("Rua A", 22)
pessoa2 = pessoa ("mario", 54, Endereco2)
pessoa2.exibir_dados()
