// -----------------------------------------
// Ejercicio 66: Matriz Transpuesta
// -----------------------------------------
// Cambia filas por columnas.

let matriz = [
    [1, 2, 3],
    [4, 5, 6]
]; // matriz original (2 filas x 3 columnas)

let transpuesta = []; // matriz vacía para guardar la transpuesta

// recorremos las columnas de la matriz original
for (let i = 0; i < matriz[0].length; i++) {
    transpuesta[i] = []; // inicializamos la fila i de la transpuesta

    // recorremos las filas de la matriz original
    for (let j = 0; j < matriz.length; j++) {
        transpuesta[i][j] = matriz[j][i]; // intercambiamos fila y columna
    }
}

console.log("Matriz transpuesta:", transpuesta); // mostramos la matriz transpuesta
