// -----------------------------------------
// Ejercicio 87: Función Recursiva Fibonacci
// -----------------------------------------
// Genera Fibonacci con recursividad.

function fibonacci(n) {
    // Caso base: si n es 0 o 1, devuelve n
    if (n <= 1) return n;
    // Llamada recursiva: suma los dos números anteriores de la serie
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Llamada correcta a la función (JavaScript es case-sensitive)
console.log("Fibonacci de 6:", fibonacci(6)); // 8
