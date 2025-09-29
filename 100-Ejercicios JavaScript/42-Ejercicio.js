// -----------------------------------------
// Ejercicio 42: Suma de Números
// -----------------------------------------
// Suma los primeros n números naturales.

let n = 10;     // límite de números a sumar
let suma = 0;   // acumulador

// Recorre del 1 hasta n
for (let i = 1; i <= n; i++) {
    suma += i; // suma cada número a la variable acumuladora
}

// Muestra el resultado final
console.log("Suma de los primeros", n, "números:", suma);
