import os

os.system ("clear")

preço = 0
pratos_solicitados = ""
lista_boleto = []
lista_pratos = []

print ('''
========= MENU =========
codigo  prato      valor
1       picanha    $9.225,00
2       piriri     $40.225,00
3       mamão      $5.200,00
4       laranja    $22.225,00
5       pao        $10.225,00
''')


while True:

    escolha = int (input("digite o codigo do pedido: "))
    
    match escolha:
        case "1":
         pratos = "picanha" 
         preço = 9.225
         lista_boleto.append(preço)
         lista_pratos.append(pratos)
        case "2":
         pratos = "piriri"
         preço =40.225
         lista_boleto.append(preço)
         lista_pratos.append(pratos)
        case "3":
         pratos = "mamão"
         preço = 5.200
         lista_boleto.append(preço)
         lista_pratos.append(pratos)
        case "4":
         pratos = "laranja"
         preço = 22.225
         lista_boleto.append(preço)
         lista_pratos.append(pratos)
        case "5":
         pratos = "pao"
         preço = 10.225
         lista_boleto.append(preço)
         lista_pratos.append(pratos)
        case _:
         pratos=""
         preço = 0
         print ("codigo invalido")

    son = (input("deseja cntinuar? use s ou n: "))
    if son == "n":
      break

    total=sum(lista_boleto)
    pratos_solicitados+="," + pratos if pratos_solicitados else pratos


print(f"pratos selecionadeos: {lista_pratos}")
print(f"valor de cada prato: {lista_boleto}")
print(f"valor total da conta: {sum(lista_boleto)}")
