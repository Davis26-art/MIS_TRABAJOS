// -----------------------------------------
// Ejercicio 64: Unión e Intersección
// -----------------------------------------
// Unión y elementos comunes de dos arrays.

let arr1 = [1, 2, 3, 4]; // primer array
let arr2 = [3, 4, 5, 6]; // segundo array

// Unión: concatenamos y eliminamos duplicados usando Set
let union = [...new Set(arr1.concat(arr2))];

// Intersección: elementos que están en ambos arrays
let interseccion = [];
for (let i = 0; i < arr1.length; i++) {
    if (arr2.includes(arr1[i])) { // si arr2 contiene el elemento de arr1
        interseccion.push(arr1[i]); // lo agregamos a intersección
    }
}

console.log("Unión:", union);           // mostramos la unión
console.log("Intersección:", interseccion); // mostramos la intersección
