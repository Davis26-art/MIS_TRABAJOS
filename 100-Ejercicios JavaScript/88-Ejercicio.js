// -----------------------------------------
// Ejercicio 88: Función de Ordenamiento
// -----------------------------------------
// Ordena un array con una función personalizada (burbuja).

function ordenarArray(arr) {
    // Bucle externo recorre todo el array
    for (let i = 0; i < arr.length; i++) {
        // Bucle interno compara elementos adyacentes
        for (let j = 0; j < arr.length - 1; j++) {
            // Si el elemento actual es mayor que el siguiente, los intercambia
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr; // Devuelve el array ordenado
}

// Ejemplo de uso
console.log("Array ordenado:", ordenarArray([5, 2, 8, 1]));
