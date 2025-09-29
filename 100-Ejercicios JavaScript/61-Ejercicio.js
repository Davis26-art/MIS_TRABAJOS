// -----------------------------------------
// Ejercicio 61: Suma de Elementos
// -----------------------------------------
// Suma todos los valores de un array.

let numeros = [5, 10, 15, 20]; // array con los números a sumar
let suma = 0;                   // inicializamos acumulador en 0

// recorremos cada elemento del array
for (let i = 0; i < numeros.length; i++) {
    suma += numeros[i]; // agregamos el valor actual a la suma
}

console.log("Suma total:", suma); // mostramos el resultado final
