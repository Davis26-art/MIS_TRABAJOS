// -----------------------------------------
// Ejercicio 86: Contador de Palabras
// -----------------------------------------
// Cuenta cuántas palabras tiene un texto.

function contarPalabras(texto) {
    // trim() elimina espacios al inicio y al final
    // split(" ") separa el texto en palabras usando el espacio como separador
    let palabras = texto.trim().split(" ");
    // length nos da la cantidad de elementos en el array, es decir, el número de palabras
    return palabras.length;
}

// Probamos la función con un ejemplo
console.log("Cantidad de palabras:", contarPalabras("Hola David cómo estás"));
