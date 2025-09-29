// -----------------------------------------
// Ejercicio 74: Filtrar Array
// -----------------------------------------
// Filtra elementos del array que cumplan una condición (>10).

let numeros = [10, 5, 20, 8, 30]; // array original
let filtrados = []; // array donde guardaremos los números que cumplan la condición

for (let i = 0; i < numeros.length; i++) { // recorremos todos los elementos
    if (numeros[i] > 10) {                // si el número es mayor a 10
        filtrados.push(numeros[i]);       // lo agregamos al array filtrados
    }
}

console.log("Números mayores a 10:", filtrados); // mostramos el array filtrado
