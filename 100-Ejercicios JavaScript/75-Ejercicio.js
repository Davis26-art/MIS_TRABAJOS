// -----------------------------------------
// Ejercicio 75: Map de Array
// -----------------------------------------
// Calcula el cuadrado de cada elemento del array.

let valores = [1, 2, 3, 4]; // array original
let cuadrados = [];         // array donde guardaremos los cuadrados

for (let i = 0; i < valores.length; i++) {  // recorremos todos los elementos
    cuadrados.push(valores[i] * valores[i]); // elevamos al cuadrado y guardamos
}

console.log("Cuadrados:", cuadrados); // mostramos el array de cuadrados
