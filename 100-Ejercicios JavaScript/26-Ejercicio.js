// -----------------------------------------
// Ejercicio 26: Sistema de Calificaciones
// -----------------------------------------

// Nota numérica (0-100)
let nota = 85;

// Switch con condición true para evaluar rangos
switch (true) {
    case (nota >= 90):              // 90-100
        console.log("Calificación: A");
        break;
    case (nota >= 80):              // 80-89
        console.log("Calificación: B");
        break;
    case (nota >= 70):              // 70-79
        console.log("Calificación: C");
        break;
    case (nota >= 60):              // 60-69
        console.log("Calificación: D");
        break;
    default:                        // menos de 60
        console.log("Calificación: F");
}
