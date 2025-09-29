// -----------------------------------------
// Ejercicio 72: Pares que Suman
// -----------------------------------------
// Encuentra todos los pares de elementos en un array cuya suma sea igual a un valor dado.

let array = [2, 4, 3, 7, 5]; // array de números
let objetivo = 9;             // valor que deben sumar los pares

// recorremos cada elemento del array
for (let i = 0; i < array.length; i++) {
    // comparamos el elemento actual con todos los siguientes
    for (let j = i + 1; j < array.length; j++) {
        if (array[i] + array[j] === objetivo) { // si la suma es igual al objetivo
            console.log("Par encontrado:", array[i], "+", array[j], "=", objetivo); // mostramos el par
        }
    }
}
