import os
from dataclasses import dataclass
os.system ("clear")
  

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

lista_livros = []
quantidade_livros = 2

au = Autor (
     nome = (input("digite o nome do autor dos livros: ")),
     biografia = ("o homen q comeu diogo")  
)
print("informe os dados sobre os livros.")
for i in range (quantidade_livros): 
    livros = Livro(

         titulo= (input("digite o titulo do livro : ")),
         ano = (input("digite o ano de publicação do livro : ")),
    )

    lista_livros.append(livros)
    print()

print("\n= exibir dados")
for livros in lista_livros:
    print(f"nome: {livros.nome}")
    print(f"ano de publicaçao: {livros.ano}")
    print(f"nome do autor : {Autor.nome}")
    print(f"biografia do autor : {Autor.biografia}")

