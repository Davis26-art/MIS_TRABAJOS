// Ejercicio 4: Calculadora básica
const prompt = require("prompt-sync")(); // Importar prompt-sync para entrada de usuario

console.log("Esta es una calculadora:");
let operador = prompt("Digita el cálculo que vas a hacer (+, -, *, /): "); // Solicitar al usuario el tipo de operación

let numero1 = Number(prompt("Digita tu el primer número: ")); // Convertir los valores ingresados a números
let numero2 = Number(prompt("Digita tu el segundo número: ")); // Convertir los valores ingresados a números

// Realizar la operación según el operador ingresado
if (operador == '+') {
    console.log("Resultado:", numero1 + numero2); // Suma
} else if (operador == '-') {
    console.log("Resultado:", numero1 - numero2); // Resta
} else if (operador == '*') {
    console.log("Resultado:", numero1 * numero2); // Multiplicación
} else if (operador == '/') {
    if (numero2 === 0) {
        console.log("No es posible dividir por 0."); // Mensaje de error
    } else {
        console.log("Resultado:", numero1 / numero2); // División
    }
} else {
    console.log("Operación inválida."); // Mensaje de error
}
