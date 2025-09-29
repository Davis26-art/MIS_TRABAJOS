// -----------------------------------------
// Ejercicio 29: Sistema de Descuentos
// -----------------------------------------

// Categoría del cliente
let categoria = "vip";

// Precio base del producto
let precioOriginal = 100;

// Variable para el precio final
let precioFinal;

// Switch según la categoría
switch (categoria) {
    case "normal":                   // sin descuento
        precioFinal = precioOriginal;
        break;
    case "estudiante":               // 10% menos
        precioFinal = precioOriginal * 0.9;
        break;
    case "vip":                      // 20% menos
        precioFinal = precioOriginal * 0.8;
        break;
    default:                         // categoría inválida
        precioFinal = precioOriginal;
}

// Imprime el precio final
console.log("Precio final:", precioFinal);
