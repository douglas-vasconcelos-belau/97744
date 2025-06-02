const readline = require("readline-sync")

const idade = readline.questionInt("digite sua idade: ")

if (idade < 16){
    console.log('nao pode votar')
}else if (idade >= 16 && idade <=17){
    console.log(`voto opicional`)
}else if (idade >= 18){
    console.log(`voto obrigatório`)
}else if (idade > 65){
console.log(`o voto não é obrigatorio`)
}