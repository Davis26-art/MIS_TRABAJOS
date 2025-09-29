// -----------------------------------------
// Ejercicio 49: Inversor de Número
// -----------------------------------------
// Invierte un número (ej: 123 → 321).

let numero = 1234;   // número a invertir
let invertido = 0;   // acumulador del número invertido

// Recorre el número mientras sea mayor que 0
for (let n = numero; n > 0; n = Math.floor(n / 10)) {
    invertido = invertido * 10 + (n % 10); // extrae y agrega la última cifra
}

// Muestra el número invertido
console.log("Número invertido:", invertido);
