// -----------------------------------------
// Ejercicio 76: Reduce de Array
// -----------------------------------------
// Suma todos los elementos de un array (simulando reduce).

let numeros = [1, 2, 3, 4, 5]; // array original
let total = 0;                // acumulador para la suma

for (let i = 0; i < numeros.length; i++) { // recorremos cada elemento
    total += numeros[i];                   // sumamos cada número al acumulador
}

console.log("Suma con reduce manual:", total); // mostramos la suma total
