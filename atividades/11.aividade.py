import os

os.system ("clear")

nume1 = float (input("digite o primeiro numero: "))
nume2 = float (input("digite o segundo numero: "))
operacao = str (input("digite a operacao desejada: "))

match operacao:
    case "+":
        resultado = nume1 + nume2
    case "/":
        resultado = nume1 / nume2
    case "*":
        resultado = nume1 * nume2
    case "-":
        resultado = nume1 - nume2
    case _:
        print ("operacao invalida.")
    
print ()
print(f"primeiro numero: {nume1}")
print(f"segundo numero: {nume2}")
print(f"operaçao: {operacao}")
print(f"resultado: {resultado}")
