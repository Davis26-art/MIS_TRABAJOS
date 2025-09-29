// -----------------------------------------
// Ejercicio 67: Diagonal Principal
// -----------------------------------------
// Suma los elementos de la diagonal principal de una matriz cuadrada.

let cuadrada = [
    [2, 0, 1],
    [3, 5, 7],
    [4, 6, 9]
]; // matriz cuadrada 3x3

let sumaDiagonal = 0; // variable para acumular la suma

// recorremos las filas de la matriz
for (let i = 0; i < cuadrada.length; i++) {
    sumaDiagonal += cuadrada[i][i]; // sumamos el elemento de la diagonal principal
}

console.log("Suma diagonal principal:", sumaDiagonal); // mostramos el resultado
