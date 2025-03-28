import os

os.system ("clear")

somaf = 0
soma = 0
contador = 0
maior_salario = 0
menor_salario = 0


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
        filhos = str (input("numero de filhos: "))
        salario = float (input("digite sua renda mensal: "))
        contador += 1
        soma += salario
        somaf += filhos

        if salario > maior_salario:
           maior_salario = salario

        if salario < menor_salario:
           menor_salario = salario

     case 2 :
         if contador > 0 :
            medias = soma / contador
            mediasf = somaf / contador
            print(f"media salarial: {medias}")
            print(f"media de filhos: {mediasf}")
            print(f"maior salario: {maior_salario}")
            print(f"menor salario: {menor_salario}")
            print(f"quantidade de familias: {contador}")
         else:
            print("nao a dados para serem exibidos.")
     case 3 :
        break
