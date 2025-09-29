// -----------------------------------------
// Ejercicio 16: Secuencia Fibonacci
// -----------------------------------------

// Cantidad de números a generar
let nFibo = 10;

// Array inicial con los dos primeros valores
let fibo = [0, 1];

// Bucle desde la posición 2 hasta nFibo
for (let i = 2; i < nFibo; i++) {
    // Agrega la suma de los dos anteriores
    fibo.push(fibo[i - 1] + fibo[i - 2]);
}

// Imprime la secuencia completa
console.log("Fibonacci:", fibo);
