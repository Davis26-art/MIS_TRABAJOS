// -----------------------------------------
// Ejercicio 70: Elementos Faltantes
// -----------------------------------------
// Encuentra los números que faltan en una secuencia de enteros.

let secuencia = [1, 2, 4, 6, 7]; // secuencia dada
let faltantes = [];               // array para guardar los números faltantes

// recorremos desde el primer hasta el último número de la secuencia
for (let i = secuencia[0]; i <= secuencia[secuencia.length - 1]; i++) {
    if (!secuencia.includes(i)) { // si el número no está en la secuencia
        faltantes.push(i);        // lo agregamos al array de faltantes
    }
}

console.log("Elementos faltantes:", faltantes); // mostramos los números faltantes
