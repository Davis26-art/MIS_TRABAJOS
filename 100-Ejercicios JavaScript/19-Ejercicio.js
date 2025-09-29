// -----------------------------------------
// Ejercicio 19: Conversor de Moneda
// -----------------------------------------

// Cantidad en dólares
let dolares = 50;

// Tasas de cambio (ejemplo)
let tasaEuro = 0.92;   // 1 USD = 0.92 EUR
let tasaPesos = 4200;  // 1 USD = 4200 COP

// Conversión a euros (2 decimales)
console.log(dolares, "USD =", (dolares * tasaEuro).toFixed(2), "EUR");

// Conversión a pesos (2 decimales)
console.log(dolares, "USD =", (dolares * tasaPesos).toFixed(2), "COP");
