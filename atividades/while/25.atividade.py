soma = 0
quantidade_notas = 2

for i in range (quantidade_notas) :
    while True:
        nota = float(input(f"digite a {i+1} nota:ª "))

        if nota < 0 or nota > 10:
            print("nota invalida< tente novamente./n")
        else:
            soma += nota
            break

media = soma / quantidade_notas

print(f"media: {media}")