import os

os.system ("clear")

soma = 0
contador = 0
mulheres5 = 0
maior_idade = 0
menor_idade = 0


while True:
    print ('''
========= MENU =========
codigo  opçoes
1       adicionar uma pessoa
2       exibir resultados  
3       sair
''')
    
    escolha = int (input("escolha uma opçao: "))
    
    match escolha :
     case 1 :
        genero = str (input("digite seu genero ultilizando m ou f: "))  
        idade = str (input("digite sua idade: "))
        salario = float (input("digite sua renda mensal: "))
        contador += 1
        soma += salario

        if idade > maior_idade:
           maior_idade = idade

        if idade < menor_idade:
           menor_idade = idade

        if genero == "f" and salario >= 5000:
           mulheres5 +=1

     case 2 :
         if contador > 0 :
            medias = soma / contador
            print(f"media salarial do grupo: {medias}")
            print(f"maior idade do grupo: {maior_idade}")
            print(f"menor idade do grupo: {menor_idade}")
            print(f"quantidade de mulheres que ganha acima de 5k: {mulheres5}")
         else:
            print("nao a dados para serem exibidos.")
     case 3 :
        break
