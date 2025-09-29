// -----------------------------------------
// Ejercicio 68: Buscar y Reemplazar
// -----------------------------------------
// Busca un valor en un array y lo reemplaza por otro.

let arreglo = [1, 2, 3, 4, 3, 5]; // array original
let buscar = 3;                   // valor a buscar
let reemplazar = 99;              // valor con el que reemplazamos

// recorremos el array
for (let i = 0; i < arreglo.length; i++) {
    if (arreglo[i] === buscar) {  // si el elemento coincide con 'buscar'
        arreglo[i] = reemplazar;  // lo reemplazamos por 'reemplazar'
    }
}

console.log("Array modificado:", arreglo); // mostramos el array modificado
