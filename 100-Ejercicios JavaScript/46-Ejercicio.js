// -----------------------------------------
// Ejercicio 46: Patrón de Asteriscos
// -----------------------------------------
// Imprime un triángulo de asteriscos.

let filas = 5; // número de filas del triángulo

// Bucle externo controla las filas
for (let i = 1; i <= filas; i++) {
    let linea = ""; // almacena los asteriscos de cada fila
    
    // Bucle interno agrega un * por cada posición
    for (let j = 1; j <= i; j++) {
        linea += "*";
    }
    
    // Muestra la fila completa
    console.log(linea);
}
