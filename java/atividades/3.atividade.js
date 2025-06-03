console.clear()

pares = 0
impares = 0

const readline = require("readline-sync")

let numero = readline.questionInt("digite o valor: ")
    
if (numero % 2 == 0){
    pares += 1
}else{
    impares += 1
}   

console.log(`qunatidade de pares: ${pares}`)
console.log(`qunatidade de impares: ${impares}`)