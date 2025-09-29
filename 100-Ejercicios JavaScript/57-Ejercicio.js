// -----------------------------------------
// Ejercicio 57: Frecuencia de Elementos
// -----------------------------------------
// Cuenta cuántas veces aparece cada número.

let numeros = [1, 2, 2, 3, 1, 4, 2]; // array con números
let frecuencia = {}; // objeto vacío donde guardaremos las frecuencias

// recorremos cada número del array
for (let i = 0; i < numeros.length; i++) {
    let num = numeros[i]; // número actual
    
    // si ya existe en el objeto, le sumamos 1
    if (frecuencia[num]) {
        frecuencia[num]++;
    } 
    // si no existe, lo inicializamos en 1
    else {
        frecuencia[num] = 1;
    }
}

console.log("Frecuencias:", frecuencia);
