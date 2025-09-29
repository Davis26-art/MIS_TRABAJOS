// -----------------------------------------
// Ejercicio 15: Factorial
// -----------------------------------------

// Número al que calculamos el factorial
let numero4 = 5;  // 5! = 120

// Variable acumuladora, arranca en 1
let factorial = 1;

// Bucle de 1 hasta numero4
for (let i = 1; i <= numero4; i++) { 
    // Multiplica acumulado por i en cada vuelta
    factorial *= i;
}

// Imprime el resultado final
console.log("El factorial de", numero4, "es:", factorial);
