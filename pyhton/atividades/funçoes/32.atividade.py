import os
os.system("cls || clear")

# funçao sem retorno.
def saudacao(nome):
    print(f"ola {nome}, bem vindo!")

nome_visitante = "douglas"
saudacao(nome_visitante) # chamando a funçao



def ds(diciplina):
    print(f"A diciplina {diciplina} faz parte do curso de Ds.")

ds_diciplina = "logica de programação"
ds(ds_diciplina)
