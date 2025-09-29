// -----------------------------------------
// Ejercicio 69: Combinar Arrays
// -----------------------------------------
// Combina dos arrays ordenados en uno solo también ordenado.

let arr1 = [1, 3, 5]; // primer array ordenado
let arr2 = [2, 4, 6]; // segundo array ordenado
let combinado = [];   // array para guardar la combinación

let i = 0, j = 0; // índices para recorrer ambos arrays

// mientras haya elementos en ambos arrays
while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {  // si elemento de arr1 es menor
        combinado.push(arr1[i]); // lo agregamos al combinado
        i++;                     // avanzamos en arr1
    } else {                    // si elemento de arr2 es menor o igual
        combinado.push(arr2[j]); // lo agregamos al combinado
        j++;                     // avanzamos en arr2
    }
}

// si quedaron elementos en arr1, los agregamos
while (i < arr1.length) {
    combinado.push(arr1[i]);
    i++;
}

// si quedaron elementos en arr2, los agregamos
while (j < arr2.length) {
    combinado.push(arr2[j]);
    j++;
}

console.log("Array combinado:", combinado); // mostramos el array final
