// -----------------------------------------
// Ejercicio 52: Multiplicación de Matrices
// -----------------------------------------
// Multiplica dos matrices válidas.

let A = [
    [1, 2],
    [3, 4]
]; // matriz 2x2

let B = [
    [2, 0],
    [1, 2]
]; // matriz 2x2

let resultado = []; // matriz resultado

// Recorre filas de A
for (let i = 0; i < A.length; i++) {
    resultado[i] = []; // crea fila
    // Recorre columnas de B
    for (let j = 0; j < B[0].length; j++) {
        let suma = 0; // acumulador para la posición [i][j]
        // Recorre elementos para multiplicar y sumar
        for (let k = 0; k < B.length; k++) {
            suma += A[i][k] * B[k][j]; // producto fila-columna
        }
        resultado[i][j] = suma; // guarda valor
    }
}

console.log("Multiplicación de matrices:", resultado);
