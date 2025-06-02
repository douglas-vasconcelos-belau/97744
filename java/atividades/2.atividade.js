console.clear()

const readline = require("readline-sync")

let va = readline.questionInt("digite o primeiro valor: ")
let vb = readline.questionInt("digite o segundo valor: ")
let vc = readline.questionInt("digite o terceiro valor: ")

resultado = va + vb

if (resultado > vc){
    console.log(`o resultado: ${resultado} é maior que ${vc} `)
}else if (resultado < vc){
    console.log(`o resultado ${resultado} é menor que ${vc}`)
}else{
    console.log(`${resultado} é igual a ${vc}`)
}