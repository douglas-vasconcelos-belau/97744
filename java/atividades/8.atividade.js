console.clear()

const readline = require("readline-sync")

const a = readline.questionInt("digite o numero A: ")
const b = readline.questionInt("digite o numero B: ")

function soma(x, y) {
    return x + y
}

function mediana(){
    return somatoria/2
}

somatoria=soma(a, b)
media=mediana()
console.log("")
console.log("soma: "+ somatoria)
console.log("")
console.log("media: "+ media)