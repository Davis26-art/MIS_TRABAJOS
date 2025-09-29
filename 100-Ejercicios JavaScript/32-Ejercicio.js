// -----------------------------------------
// Ejercicio 32: Sistema de Transporte
// -----------------------------------------

// Tipo de transporte
let transporte = "bus"; // taxi, bus, tren

// Distancia recorrida en km
let distancia = 10;

// Variable para la tarifa
let tarifa;

// Switch según transporte
switch (transporte) {
    case "taxi":                   // $2 por km
        tarifa = distancia * 2;
        break;
    case "bus":                    // $1 por km
        tarifa = distancia * 1;
        break;
    case "tren":                   // $0.5 por km
        tarifa = distancia * 0.5;
        break;
    default:                       // transporte inválido
        tarifa = 0;
}

// Imprime la tarifa calculada
console.log("Tarifa:", tarifa);
