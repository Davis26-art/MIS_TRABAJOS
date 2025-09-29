// -----------------------------------------
// Ejercicio 56: Promedio de Array
// -----------------------------------------
// Calcula el promedio de los elementos.

let notas = [10, 8, 9, 7, 6]; // array con calificaciones
let sumaNotas = 0; // acumulador inicializado en 0

// recorremos el array sumando todas las notas
for (let i = 0; i < notas.length; i++) {
    sumaNotas += notas[i]; // en cada vuelta agregamos la nota actual
}

// el promedio es la suma dividida entre la cantidad de notas
let promedio = sumaNotas / notas.length;

console.log("Promedio:", promedio);
