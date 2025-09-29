// -----------------------------------------
// Ejercicio 63: Rotación de Array
// -----------------------------------------
// Rota los elementos k posiciones a la derecha.

let arr = [1, 2, 3, 4, 5]; // array original
let k = 2;                  // número de posiciones a rotar

// repetimos k veces: movemos el último elemento al inicio
for (let i = 0; i < k; i++) {
    arr.unshift(arr.pop()); // 'pop' saca el último, 'unshift' lo pone al inicio
}

console.log("Array rotado:", arr); // mostramos el array final
