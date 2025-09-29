// -----------------------------------------
// Ejercicio 43: Factorial con For
// -----------------------------------------
// Calcula el factorial usando un bucle for.

let numFact = 6;    // número a calcular
let factorial = 1;  // acumulador inicial

// Recorre del 1 hasta numFact
for (let i = 1; i <= numFact; i++) {
    factorial *= i; // multiplica acumulando
}

// Muestra el resultado
console.log("Factorial de", numFact, "es:", factorial);
