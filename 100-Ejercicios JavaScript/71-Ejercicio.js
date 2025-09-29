// -----------------------------------------
// Ejercicio 71: Subarray Máximo
// -----------------------------------------
// Encuentra el subarray con la suma máxima usando el algoritmo de Kadane.

let nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]; // array de números
let maxActual = nums[0]; // máximo actual en la iteración
let maxTotal = nums[0];  // máximo global encontrado hasta ahora

// recorremos desde el segundo elemento
for (let i = 1; i < nums.length; i++) {
    // maxActual es el mayor entre el número actual solo o sumarlo al subarray anterior
    maxActual = Math.max(nums[i], maxActual + nums[i]);
    
    // actualizamos el máximo global si el actual es mayor
    if (maxActual > maxTotal) {
        maxTotal = maxActual;
    }
}

console.log("Suma máxima de subarray:", maxTotal); // mostramos la suma máxima
