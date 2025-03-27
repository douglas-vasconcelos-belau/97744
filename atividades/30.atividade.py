import os

os.system ("clear")

mulher = 0
pessoa = 0
mascu = "m"
femi = "f"
sim = "sim"


while True :
    sexo = str (input("qual seu sexo: "))
    
    if sexo != femi and sexo != mascu :
        print ("genero apresentado nao existente.")
        break
     
    if sexo == femi :
       
       idade = int (input("digite sua idade:"))
       salariof = float (input("digite seu salario: "))
       para = str (input("deseja incerar? : "))
       soma = pessoa + 1
    
    if salariof >= 5000:
       mulher +1
       
    
    if sexo == mascu :
    
     idade = int (input("digite sua idade:"))
     salario = float (input("digite seu salario: "))
     para = str (input("deseja incerar? : "))
     soma = pessoa + 1
    
    
    if para == sim :
        mediasalarial = (salario + salariof) / soma
        #idademin = min (idade)


        print()
        print(f"media salarial do grupo: {mediasalarial}")
        #print(f"menor idade do grupo: {idademin}")
        print(f"quantidade de mulheres que recebem mais de $5.000 no grupo: {salariof}")
        break

