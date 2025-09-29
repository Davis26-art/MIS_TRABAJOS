// -----------------------------------------
// Ejercicio 51: Suma de Matrices
// -----------------------------------------
// Suma dos matrices de igual tamaño.

let matriz1 = [
    [1, 2],
    [3, 4]
]; // primera matriz

let matriz2 = [
    [5, 6],
    [7, 8]
]; // segunda matriz

let sumaMatriz = []; // matriz resultado

// Recorre filas
for (let i = 0; i < matriz1.length; i++) {
    sumaMatriz[i] = []; // crea subarreglo por fila
    // Recorre columnas
    for (let j = 0; j < matriz1[i].length; j++) {
        sumaMatriz[i][j] = matriz1[i][j] + matriz2[i][j]; // suma elemento a elemento
    }
}

console.log("Suma de matrices:", sumaMatriz);
