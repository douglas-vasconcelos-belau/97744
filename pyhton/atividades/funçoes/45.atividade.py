import os

os.system ("clear")

peso = float(input("digite seu peso em kilos :"))
altura = float(input("digite sua altura em metros :"))

def massa ():
    al = altura * altura
    imc = peso / al
    return imc

imc = massa()

if imc <18.5:
    print("abaixo do peso | consulte um lutricionista para orientaçao")
elif imc >= 18.5 and imc <= 24.9:
    print("peso normal | mantenha habitos saudaveis")
elif imc >= 25 and imc <= 29.9:
    print("sobrepeso | considere uma dieta balanceada e atividade fisica")
elif imc >= 30 and imc <= 34.9:
    print("obesidade grau 1 | procure orientaçao de um profissional da saude")
elif imc >= 35 and imc <= 39.9:
    print("obesidade grau 2 | consulte um medico para avaliaçao profissional")
elif imc >= 40:
    print("obesidade grau 3 | busque assistencia media imediatamente")