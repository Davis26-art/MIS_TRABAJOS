// -----------------------------------------
// Ejercicio 79: Rotar Matriz 90°
// -----------------------------------------
// Gira una matriz cuadrada 90° en sentido horario.

let original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let rotada = [];  // matriz resultante

for (let i = 0; i < original.length; i++) {       // recorremos las filas de la nueva matriz
    rotada[i] = [];
    for (let j = 0; j < original.length; j++) {   // recorremos las columnas
        // el elemento (i, j) de la matriz rotada se toma desde (N-1-j, i) de la original
        rotada[i][j] = original[original.length - 1 - j][i];
    }
}

console.log("Matriz rotada 90°:", rotada);
