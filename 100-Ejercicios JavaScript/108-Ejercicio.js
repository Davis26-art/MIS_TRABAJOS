// -----------------------------------------
// Ejercicio 108: Descuento por Edad
// -----------------------------------------

let edadCliente = 65;  // Edad del cliente

// Usamos un ternario para determinar el descuento
let descuento = (edadCliente >= 60) 
                ? "20% de descuento" // Si tiene 60 o más → descuento del 20%
                : "Sin descuento";   // Si es menor de 60 → no hay descuento

console.log("Cliente de", edadCliente, "años:", descuento);
// Muestra: "Cliente de 65 años: 20% de descuento"
