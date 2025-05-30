import os
from datetime import datetime
os.system ("clear")

anona = int(input("digite o ano de seu nascimento:"))

def idade():
    idadeu = datetime.now().year - anona
    return idadeu

idadeu = idade()

print (f"a sua idade é : {idadeu}")