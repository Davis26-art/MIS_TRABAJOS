// -----------------------------------------
// Ejercicio 39: Conversor de Bases
// -----------------------------------------
// Convierte un número decimal a otra base.

let numeroDec = 42;    // número en decimal
let base = "binario";  // opciones: binario o hexadecimal

switch (base) {
    case "binario":
        // .toString(2) → convierte a base 2 (binario)
        console.log(numeroDec, "en binario =", numeroDec.toString(2));
        break;
    case "hexadecimal":
        // .toString(16) → convierte a base 16 (hexadecimal)
        console.log(numeroDec, "en hexadecimal =", numeroDec.toString(16));
        break;
    default:
        // Si la base no es válida
        console.log("Base no válida");
}
