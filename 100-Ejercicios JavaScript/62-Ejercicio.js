// -----------------------------------------
// Ejercicio 62: Elementos Únicos
// -----------------------------------------
// Muestra los elementos que no se repiten.

let array = [1, 2, 2, 3, 4, 4, 5]; // array original
let unicos = [];                   // array donde guardaremos los elementos únicos

// recorremos cada elemento del array
for (let i = 0; i < array.length; i++) {
    let num = array[i]; // número actual
    let contador = 0;   // contador de apariciones

    // contamos cuántas veces aparece 'num' en el array
    for (let j = 0; j < array.length; j++) {
        if (array[j] === num) contador++;
    }

    // si aparece solo una vez, lo agregamos a 'unicos'
    if (contador === 1) {
        unicos.push(num);
    }
}

console.log("Elementos únicos:", unicos); // mostramos los elementos que no se repiten
