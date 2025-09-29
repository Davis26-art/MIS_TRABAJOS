// -----------------------------------------
// Ejercicio 78: Simetría de Matriz
// -----------------------------------------
// Comprueba si una matriz cuadrada es simétrica (matriz[i][j] == matriz[j][i]).

let matriz = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
];

let simetrica = true;  // asumimos que sí es simétrica inicialmente

for (let i = 0; i < matriz.length; i++) {       // recorremos filas
    for (let j = 0; j < matriz.length; j++) {   // recorremos columnas
        if (matriz[i][j] !== matriz[j][i]) {    // si algún elemento no coincide con su transpuesta
            simetrica = false;                  // no es simétrica
            break;                              
        }
    }
}

console.log("¿Es simétrica?", simetrica); // imprime true o false
