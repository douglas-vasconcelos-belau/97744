import os

os.system ("clear")

print ('''
========= MENU =========
codigo  prato      valor
1       picanha    $9.225,00
2       piriri     $40.225,00
3       mamão      $5.200,00
4       laranja    $22.225,00
5       pao        $10.225,00
''')

escolha = int (input("digite o codigo do pedido: "))

match escolha:
    case "1":
     print("picanha: $9.225,00")
    case "2":
     print("piriri: $9.225,00")
    case "3":
     print("mamão: $9.225,00")
    case "4":
     print("laranja: $9.225,00")
    case "5":
     print("pao: $9.225,00")
    case _:
     print ("codigo invalido")