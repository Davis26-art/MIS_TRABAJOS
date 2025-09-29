// -----------------------------------------
// Ejercicio 98: Generador de Reportes
// -----------------------------------------
// Crea un reporte simple a partir de un array de datos

function generarReporte(datos) {
    console.log("----- REPORTE -----"); // Encabezado del reporte

    // Recorre cada elemento del array 'datos'
    for (let i = 0; i < datos.length; i++) {
        // Imprime el índice (sumando 1 para que empiece desde 1) y el contenido
        console.log("Item", i + 1, ":", datos[i]);
    }

    console.log("-------------------"); // Pie de página del reporte
}

// Llamada a la función con un array de ejemplo
generarReporte(["Venta 1: $100", "Venta 2: $200"]);
