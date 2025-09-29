// -----------------------------------------
// Ejercicio 65: Array Invertido
// -----------------------------------------
// Crea un nuevo array con los elementos en orden inverso.

let original = [10, 20, 30, 40]; // array original
let invertido = [];               // array vacío donde guardaremos los elementos invertidos

// recorremos el array desde el último elemento hasta el primero
for (let i = original.length - 1; i >= 0; i--) {
    invertido.push(original[i]); // agregamos cada elemento al nuevo array
}

console.log("Array invertido:", invertido); // mostramos el array invertido
