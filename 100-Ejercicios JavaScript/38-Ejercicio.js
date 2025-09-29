// -----------------------------------------
// Ejercicio 38: Sistema de Puntos
// -----------------------------------------
// Fórmula general: puntos = compra * porcentaje

let categoriaCliente = "oro"; // tipo de cliente
let compra = 200;             // valor de la compra
let puntos;

// Según categoría, se aplica un porcentaje distinto
switch (categoriaCliente) {
    case "normal":                   // clientes normales: 5% en puntos
        puntos = compra * 0.05;
        break;
    case "plata":                    // clientes plata: 10% en puntos
        puntos = compra * 0.1;
        break;
    case "oro":                      // clientes oro: 20% en puntos
        puntos = compra * 0.2;
        break;
    default:                         // si la categoría no existe
        puntos = 0;
}

// Muestra los puntos generados
console.log("Puntos obtenidos:", puntos);
