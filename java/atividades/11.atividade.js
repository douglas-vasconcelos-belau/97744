const listadenumeros = [1,2,-3,4,5]
let listapositivos = 0
let listanegativos = 0
let soma = 0
console.clear()

console.log(`= filtrando numeros =`)
listadenumeros.forEach(num =>{
    if (num < 0){
        listanegativos += 1
    }else if(num > 0){
      soma += num
    }   
})

console.log("quantidade positivo")
console.log (soma)
console.log("quantidade negativo")
console.log(listanegativos)