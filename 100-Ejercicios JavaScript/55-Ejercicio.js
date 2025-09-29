// -----------------------------------------
// Ejercicio 55: Máximo y Mínimo
// -----------------------------------------
// Encuentra el mayor y menor en un array.

let datos = [15, 3, 9, 22, 7]; // array de números
let max = datos[0]; // asumimos que el primero es el mayor
let min = datos[0]; // asumimos que el primero es el menor

// recorremos desde el segundo elemento
for (let i = 1; i < datos.length; i++) {
    if (datos[i] > max) max = datos[i]; // si encontramos algo mayor → actualizamos max
    if (datos[i] < min) min = datos[i]; // si encontramos algo menor → actualizamos min
}

console.log("Máximo:", max, " Mínimo:", min);
