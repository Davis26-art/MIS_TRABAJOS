// -----------------------------------------
// Ejercicio 81: Función de Validación
// -----------------------------------------
// Valida si un dato es número, string o boolean.

function validarDato(dato) {
    // typeof devuelve el tipo de dato: number, string, boolean, object, etc.

    if (typeof dato === "number") {
        console.log(dato, "es un número");  // si es número
    } else if (typeof dato === "string") {
        console.log(dato, "es una cadena de texto"); // si es texto
    } else if (typeof dato === "boolean") {
        console.log(dato, "es un booleano"); // si es verdadero/falso
    } else {
        console.log(dato, "es de otro tipo"); // cualquier otro tipo (objeto, null, undefined, etc.)
    }
}

// Pruebas
validarDato(123);     // "123 es un número"
validarDato("Hola");  // "Hola es una cadena de texto"
validarDato(true);    // "true es un booleano"
