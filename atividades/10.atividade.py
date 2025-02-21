import os

os.system ("clear")

maça = 1.30
desconto = 1.00
quantidade = float (input("digite a quantidade de maças: "))
preço = (maça * quantidade)
preço2 = (desconto * quantidade)

if quantidade >= 12 :
    print(f"o valor da sua compra é: {preço:.2f}") 
else:
    print (f"o valor da sua compra é: {preço2:.2f}")

#forma do professor

quantidade_maça = int (input("a qualtidade de mças:"))

if quantidade_maça < 12 :
    preço_da_maça = 1.30
else:
    preço_da_maça = 1.00

    valor_total = quantidade_maça * preço_da_maça

    print ()
    print (f"o valor da compra é: {valor_total:.2f}")



