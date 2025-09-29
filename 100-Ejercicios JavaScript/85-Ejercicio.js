// -----------------------------------------
// Ejercicio 85: Formateador de Fechas
// -----------------------------------------
// Convierte fechas al formato dd/mm/aaaa

function formatearFecha(fecha) {
    let d = fecha.getDate();          // obtiene el día del mes (1-31)
    let m = fecha.getMonth() + 1;     // obtiene el mes (0-11), por eso se suma 1
    let a = fecha.getFullYear();      // obtiene el año completo

    // devuelve la fecha en formato dd/mm/aaaa
    // si día o mes son menores a 10, agrega un 0 delante
    return (d < 10 ? "0" + d : d) + "/" + 
           (m < 10 ? "0" + m : m) + "/" + a;
}

// Probamos la función con la fecha actual
console.log("Fecha formateada:", formatearFecha(new Date()));
