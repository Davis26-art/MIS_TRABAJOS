// -----------------------------------------
// Ejercicio 14: Número Primo
// -----------------------------------------
// Un número primo solo es divisible por 1 y por sí mismo.

let numero3 = 17;
let esPrimo = true;

if (numero3 <= 1) { // Los números menores o iguales a 1 no son primos
    esPrimo = false;
} else { // Verifica divisibilidad desde 2 hasta la raíz cuadrada del número
    for (let i = 2; i < numero3; i++) {
        if (numero3 % i === 0) {
            esPrimo = false; 
            break;
        }
    }
}

console.log(numero3, esPrimo ? "es PRIMO" : "NO es primo");
