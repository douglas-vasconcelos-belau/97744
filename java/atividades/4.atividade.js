console.clear()

const readline = require("readline-sync")

const dia = readline.questionInt("digite o dia da semana dia: ")

if (dia == 1){
    console.log('domingo: não é dia util')
}else if (dia == 2 ){
    console.log(`segunda-feira: é dia util`)
}else if (dia == 3){
    console.log(`terça-feira: é dia util`)
}else if (dia == 4){
console.log(`quarta-feira: é dia util`)
}else if (dia == 5){
console.log(`quinta-feira: é dia util`)
}else if (dia == 6){
console.log(`sexta-feira: é dia util`)
}else if (dia == 7){
console.log(`sabado: não é dia util`)
}else{
    print("numero invalido")
}