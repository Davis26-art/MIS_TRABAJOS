// -----------------------------------------
// Ejercicio 34: Calculadora Científica Básica
// -----------------------------------------

// Tipo de operación: "raiz" o "potencia"
let oper = "raiz";

// Números de entrada
let numX = 9;
let numY = 3;

// Switch según la operación
switch (oper) {
    case "raiz":                                  // raíz cuadrada
        console.log("Raíz cuadrada:", Math.sqrt(numX));
        break;
    case "potencia":                              // numX elevado a numY
        console.log("Potencia:", Math.pow(numX, numY));
        break;
    default:                                      // opción no reconocida
        console.log("Operación no válida");
}
