const listadenumeros = [1,2,3,4,5,6]
let listapares = 0
let listaimpares = 0
console.clear()
console.log(`= filtrando numeros pares =`)

listadenumeros.forEach(num =>{
    if (num % 2 == 0){
     listapares+=1
    }else{
      listaimpares+=1
    }   
})

console.log("quantidade impares")
console.log (listaimpares)
console.log("quantidade pares")
console.log(listapares)