// -----------------------------------------
// Ejercicio 95: Función de Búsqueda Binaria
// -----------------------------------------
// Busca un elemento en un array ordenado.

function busquedaBinaria(arr, objetivo) {
    let inicio = 0, fin = arr.length - 1;

    while (inicio <= fin) {
        // Calcula el índice del elemento medio
        let medio = Math.floor((inicio + fin) / 2);

        if (arr[medio] === objetivo) {
            return medio; // Elemento encontrado, retorna índice
        } else if (arr[medio] < objetivo) {
            // Si el medio es menor que el objetivo, buscar a la derecha
            inicio = medio + 1;
        } else {
            // Si el medio es mayor que el objetivo, buscar a la izquierda
            fin = medio - 1;
        }
    }

    return -1; // Elemento no encontrado
}

let numeros = [1, 3, 5, 7, 9, 11];

console.log("Índice de 7:", busquedaBinaria(numeros, 7)); // 3
console.log("Índice de 4:", busquedaBinaria(numeros, 4)); // -1
