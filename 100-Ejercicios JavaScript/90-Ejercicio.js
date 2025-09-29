// -----------------------------------------
// Ejercicio 90: Calculadora Estadística
// -----------------------------------------
// Media, mediana y moda de un array.

function estadisticas(arr) {
    // --- Media ---
    let suma = 0;
    for (let i = 0; i < arr.length; i++) suma += arr[i]; // suma todos los números
    let media = suma / arr.length;                        // divide por la cantidad de números

    // --- Mediana ---
    arr.sort((a, b) => a - b);                            // ordena de menor a mayor
    let mitad = Math.floor(arr.length / 2);
    let mediana = arr.length % 2 === 0 ?
        (arr[mitad - 1] + arr[mitad]) / 2 : arr[mitad];  // si es par, promedio de los del medio; si no, el del medio

    // --- Moda ---
    let freq = {};       // objeto para contar frecuencias
    let maxFreq = 0;
    let moda;
    for (let num of arr) {
        freq[num] = (freq[num] || 0) + 1;  // aumenta contador
        if (freq[num] > maxFreq) {         // si es la frecuencia más alta hasta ahora
            maxFreq = freq[num];
            moda = num;
        }
    }

    return { media, mediana, moda };
}

// Ejemplo de uso
console.log("Estadísticas:", estadisticas([1, 2, 2, 3, 4]));
