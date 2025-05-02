import os
os.system("clear")

login = "q"
senha = "q"
senha_c = str (input("digite sua senha: "))
login_c = str (input("digite seu usuario: "))
os.system("clear")

if login_c == login and senha_c == senha:

    salario_b = float(input("digite seu salario base: "))
    dependentes = int(input("digite a quantidade de dependentes: "))
    vale_trans = str(input("deseja vale transporte ? : "))
    vale_refei = str(input("didgite o valor do vale refeiçao: "))
    os.system("clear")

    desconto_vale = vale_refei * 0.20
    desconto_palno_de_saude = 150.00 * dependentes
    reduçao_d = 189.59 * dependentes  
     
    if vale_trans == "s":
     desconto_trans = vale_trans * 0.06
    elif vale_trans == "n":
     desconto_trans = 0
        
    def inss (salario_inss):
      
      if salario_b <=  1518.00:
        return salario_inss == salario_b * 0.075 
      elif salario_b <= 2793.88:
        return salario_inss == salario_b * 0.9 - 113.85
      elif salario_b <=4190.83 :
        return salario_inss == salario_b * 0.12 - 189.54
      elif salario_b <= 8157.41 :
        return salario_inss == salario_b * 0.14 - 318.38

      
      
    def irr (irrf):
       




else:
 print("acesso negado")


