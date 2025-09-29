// -----------------------------------------
// Ejercicio 25: Conversor de Unidades
// -----------------------------------------

// Valor en metros
let valor = 2;

// Unidad destino (cm, km, pulgadas)
let unidad = "km";

// Switch según la unidad
switch (unidad) {
    case "cm":                   // metros → centímetros
        console.log(valor, "m =", valor * 100, "cm");
        break;
    case "km":                   // metros → kilómetros
        console.log(valor, "m =", valor / 1000, "km");
        break;
    case "pulgadas":             // metros → pulgadas
        console.log(valor, "m =", valor * 39.37, "pulgadas");
        break;
    default:                     // unidad inválida
        console.log("Unidad no válida");
}
