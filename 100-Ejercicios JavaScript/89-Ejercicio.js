// -----------------------------------------
// Ejercicio 89: Manipulador de Strings
// -----------------------------------------
// Diferentes operaciones sobre un string.

function manipularCadena(texto) {
    console.log("Original:", texto);                 // Muestra el string tal cual
    console.log("Mayúsculas:", texto.toUpperCase()); // Convierte todo a mayúsculas
    console.log("Minúsculas:", texto.toLowerCase()); // Convierte todo a minúsculas
    console.log("Longitud:", texto.length);          // Número de caracteres
    console.log("Primera letra:", texto[0]);         // Primer carácter del string
}

// Llamada de ejemplo
manipularCadena("Programar");
