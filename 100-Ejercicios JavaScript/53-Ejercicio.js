// -----------------------------------------
// Ejercicio 53: Búsqueda en Array
// -----------------------------------------
// Busca un elemento en un array.

let numeros = [10, 20, 30, 40, 50]; // arreglo de números
let buscado = 30;                   // número que queremos encontrar
let encontrado = false;             // bandera para saber si aparece

// Recorre el array
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] === buscado) { // compara el valor actual con el buscado
        encontrado = true;        // lo encontró
        break;                    // corta el ciclo
    }
}

// Operador ternario: elige mensaje según la condición
console.log(encontrado ? "Encontrado" : "No encontrado");
