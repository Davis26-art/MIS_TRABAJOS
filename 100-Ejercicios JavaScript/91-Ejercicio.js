// -----------------------------------------
// Ejercicio 91: Conversor de Bases con Funciones
// -----------------------------------------
// Convierte un número decimal a binario o hexadecimal.

function convertirBase(numero, base) {
    if (base === "binario") {
        return numero.toString(2);   // convierte el número a base 2 (binario)
    } else if (base === "hexadecimal") {
        return numero.toString(16);  // convierte el número a base 16 (hexadecimal)
    } else {
        return "Base no soportada";  // si no es binario ni hexadecimal
    }
}

// Ejemplos de uso
console.log("42 en binario:", convertirBase(42, "binario"));       // "101010"
console.log("42 en hexadecimal:", convertirBase(42, "hexadecimal")); // "2a"
