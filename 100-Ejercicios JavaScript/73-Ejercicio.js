// -----------------------------------------
// Ejercicio 73: Array de Objetos
// -----------------------------------------
// Ordena un array de objetos según la propiedad 'edad'.

let personas = [
    { nombre: "Ana", edad: 25 },   // objeto 1
    { nombre: "Luis", edad: 30 },  // objeto 2
    { nombre: "Marta", edad: 20 }  // objeto 3
];

// usamos sort con función de comparación para ordenar por edad
personas.sort((a, b) => a.edad - b.edad); // menor a mayor

console.log("Personas ordenadas por edad:", personas); // mostramos el resultado
