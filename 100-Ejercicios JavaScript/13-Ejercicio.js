// -----------------------------------------
// Ejercicio 13: Suma de Dígitos
// -----------------------------------------
// Suma los dígitos de un número.

let numero2 = 456;  // 4 + 5 + 6 = 15
let suma = 0;

for (let i = 0; i < numero2.toString().length; i++) { // Recorre cada dígito
    suma += parseInt(numero2.toString()[i]); // Convierte el carácter a número y suma
}
console.log("La suma de los dígitos es:", suma);
