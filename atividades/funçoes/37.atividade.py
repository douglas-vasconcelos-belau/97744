import os

os.system ("clear")

def somar (n1, n2) :
    calcular = n1 + n2
    return calcular

def subtrair (n1, n2):
    calcular = n1 - n2 
    return calcular

def mult (n1,n2):
    calcular = n1 * n2
    return calcular

def div (n1,n2):
    calcular = n1 / n2
    return calcular

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))

soma = somar(n1,n2)
subtracao = subtrair(n1,n2)
multi = mult (n1,n2)
divi = div(n1,n2) 


print (f"soma: {soma}")
print (f"subtração: {subtracao}")
print (f"divisão: {divi}")
print (f"multiplicação: {multi}")