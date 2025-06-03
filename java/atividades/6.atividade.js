console.clear()

const readline = require("readline-sync")

const a = readline.questionInt("digite o dia A: ")
const b = readline.questionInt("digite o dia B: ")

function soma(a, b) {
    return a + b
}
function sub(a, b) {
    return a - b
}
function div(a, b) {
    return a / b
}
function mul(a, b) {
    return a * b
}

const somari = soma(a,b)
const subi =  sub(a,b)
const divi =  div(a,b)
const mult =  mul(a,b)

console.log(`soma: ${somari}`)
console.log(`subitração: ${subi}`)
console.log(`divisão: ${divi}`)
console.log(`multiplicação: ${mult}`)