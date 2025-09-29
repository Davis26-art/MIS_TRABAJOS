// -----------------------------------------
// Ejercicio 77: Matriz Identidad
// -----------------------------------------
// Crea una matriz identidad de tamaño n x n.

let n = 4;              // tamaño de la matriz
let identidad = [];      // inicializamos la matriz

for (let i = 0; i < n; i++) {   // recorremos las filas
    identidad[i] = [];           // creamos la fila i
    for (let j = 0; j < n; j++) {       // recorremos las columnas
        identidad[i][j] = (i === j ? 1 : 0); // 1 si estamos en la diagonal, 0 si no
    }
}

console.log("Matriz identidad:", identidad); // mostramos la matriz completa
