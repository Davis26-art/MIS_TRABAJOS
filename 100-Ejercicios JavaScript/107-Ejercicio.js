// -----------------------------------------
// Ejercicio 107: Día Laboral
// -----------------------------------------

let dia = "domingo";  // Definimos el día a evaluar

// Evaluamos si el día es sábado o domingo
let esLaboral = (dia === "sábado" || dia === "domingo") 
                ? "Fin de semana"  // Si es sábado o domingo → Fin de semana
                : "Laboral";        // Si no → Laboral

console.log(dia, "es", esLaboral); // Muestra: "domingo es Fin de semana"
