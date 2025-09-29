// -----------------------------------------
// Ejercicio 58: Fibonacci con Array
// -----------------------------------------
// Genera Fibonacci y lo guarda en un array.

let n = 10;           // cantidad de números de la serie
let fibo = [0, 1];    // empezamos con los dos primeros términos

// desde la posición 2 en adelante, cada número es la suma de los dos anteriores
for (let i = 2; i < n; i++) {
    fibo[i] = fibo[i - 1] + fibo[i - 2];
}

console.log("Serie Fibonacci:", fibo);
