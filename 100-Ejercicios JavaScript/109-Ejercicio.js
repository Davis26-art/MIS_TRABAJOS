// -----------------------------------------
// Ejercicio 109: Tipo de Triángulo
// -----------------------------------------

let x = 4, y = 4, z = 6;  // Lados del triángulo

// Usamos ternarios encadenados para clasificar
let tipoTriangulo = (x === y && y === z) ? "Equilátero" :  // Todos iguales → Equilátero
                    (x === y || y === z || x === z) ? "Isósceles" : // Dos iguales → Isósceles
                    "Escaleno"; // Ninguno igual → Escaleno

console.log("Triángulo:", tipoTriangulo);
// Muestra: "Triángulo: Isósceles"
