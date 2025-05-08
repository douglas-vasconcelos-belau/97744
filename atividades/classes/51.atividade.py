import os
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = pessoa("alice", 30,56.7,1.50)
pessoa2 = pessoa ("carlos", 58,70.7,33)

print(f"nome: {pessoa1.nome}, idade {pessoa1.idade}, peso {pessoa1.peso}, altura {pessoa1.altura}.")
print(f"nome: {pessoa2.nome}, idade {pessoa2.idade}, peso {pessoa2.peso}, altura {pessoa2.altura}.")
