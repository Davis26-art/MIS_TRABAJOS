// -----------------------------------------
// Ejercicio 40: Simulador de Cajero Automático
// -----------------------------------------
// Acciones posibles: consultar, retirar o depositar.

let saldo = 500;        // saldo inicial en la cuenta
let accion = "retirar"; // acción elegida
let monto = 100;        // cantidad a retirar o depositar

switch (accion) {
    case "consultar":
        // Muestra el saldo actual
        console.log("Saldo actual:", saldo);
        break;
    case "retirar":
        // Verifica si hay suficiente saldo
        if (monto <= saldo) {
            saldo -= monto; // resta el monto al saldo
            console.log("Retiro exitoso. Nuevo saldo:", saldo);
        } else {
            console.log("Fondos insuficientes"); // no alcanza el saldo
        }
        break;
    case "depositar":
        saldo += monto; // suma el monto al saldo
        console.log("Depósito exitoso. Nuevo saldo:", saldo);
        break;
    default:
        // Si la acción no coincide con ninguna opción
        console.log("Operación no válida");
}
