// -----------------------------------------
// Ejercicio 21: Calculadora con Switch
// -----------------------------------------

// Números a operar
let numA = 8;
let numB = 4;

// Operación a realizar
let operacion = "multiplicar"; // opciones: sumar, restar, multiplicar, dividir

// Estructura switch según la operación
switch (operacion) {
    case "sumar":               // si operacion = "sumar"
        console.log("Resultado:", numA + numB);
        break;
    case "restar":              // si operacion = "restar"
        console.log("Resultado:", numA - numB);
        break;
    case "multiplicar":         // si operacion = "multiplicar"
        console.log("Resultado:", numA * numB);
        break;
    case "dividir":             // si operacion = "dividir"
        console.log("Resultado:", numA / numB);
        break;
    default:                    // si no coincide con ninguna
        console.log("Operación no válida");
}
