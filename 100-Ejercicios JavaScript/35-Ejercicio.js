// -----------------------------------------
// Ejercicio 35: Sistema de Nómina
// -----------------------------------------

// Tipo de contrato: fijo, temporal o freelance
let contrato = "temporal";

// Horas trabajadas en la semana
let horasTrab = 40;

// Variable para guardar el pago calculado
let pago;

// Switch según tipo de contrato
switch (contrato) {
    case "fijo":                 // contrato fijo: $15 por hora
        pago = horasTrab * 15;
        break;
    case "temporal":             // contrato temporal: $12 por hora
        pago = horasTrab * 12;
        break;
    case "freelance":            // contrato freelance: $20 por hora
        pago = horasTrab * 20;
        break;
    default:                     // si no coincide con ningún contrato
        pago = 0;
}

// Mostrar resultado final
console.log("Pago total:", pago);
