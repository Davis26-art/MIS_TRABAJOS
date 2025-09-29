// -----------------------------------------
// Ejercicio 80: Camino en Matriz
// -----------------------------------------
// Ejemplo simple: recorrer de izquierda a derecha (fila por fila).

let caminoMatriz = [
    [1, 2, 3],
    [4, 5, 6]
];

let recorrido = [];  // guardará los elementos en orden de recorrido

for (let i = 0; i < caminoMatriz.length; i++) {      // recorre cada fila
    for (let j = 0; j < caminoMatriz[i].length; j++) { // recorre cada columna de la fila
        recorrido.push(caminoMatriz[i][j]);          // agrega el elemento al array "recorrido"
    }
}

console.log("Recorrido de la matriz:", recorrido);
