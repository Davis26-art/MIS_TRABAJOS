// -----------------------------------------
// Ejercicio 54: Ordenamiento Burbuja
// -----------------------------------------
// Ordena un array de menor a mayor.

let lista = [5, 3, 8, 1, 2]; // array desordenado

// Recorre todo el array varias veces
for (let i = 0; i < lista.length; i++) {
    // Compara elementos adyacentes
    for (let j = 0; j < lista.length - 1; j++) {
        if (lista[j] > lista[j + 1]) {     // si el actual es mayor al siguiente
            let temp = lista[j];           // guarda el actual en temp
            lista[j] = lista[j + 1];       // mueve el siguiente hacia atrás
            lista[j + 1] = temp;           // coloca temp (el mayor) adelante
        }
    }
}

console.log("Array ordenado:", lista); // muestra ya ordenado
