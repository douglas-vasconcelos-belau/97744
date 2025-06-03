//arrow function

const readline = require("readline-sync")

const a = readline.questionInt("digite o numero A: ")
const b = readline.questionInt("digite o numero B: ")

function soma(a, b) {
    return a + b
}
function mul(a, b) {
    return a * b
}

const subitrair = (a, b) => a - b
const dividir = (a, b) => a / b

const soma =  somar(2,3)
const mul =  multiplicar(2,3)
const div =  dividir(2,3)
const subitracao = subitrair(2,3)

console.log(`subtração: ${subitracao}`)
console.log(`soma: ${somar}`)
console.log(`divisão: ${div}`)
console.log(`multiplicação: ${multiplicar}`)