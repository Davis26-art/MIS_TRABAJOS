// -----------------------------------------
// Ejercicio 33: Conversor de Tiempo
// -----------------------------------------

// Segundos a convertir
let segundos = 3600;

// Unidad destino: "minutos" o "horas"
let unidadTiempo = "horas";

// Switch según unidad de tiempo
switch (unidadTiempo) {
    case "minutos":                          // pasa a minutos
        console.log(segundos, "seg =", segundos / 60, "minutos");
        break;
    case "horas":                            // pasa a horas
        console.log(segundos, "seg =", segundos / 3600, "horas");
        break;
    default:                                 // unidad inválida
        console.log("Unidad no válida");
}
