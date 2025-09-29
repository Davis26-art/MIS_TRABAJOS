// -----------------------------------------
// Ejercicio 106: Nota a Letra
// -----------------------------------------

let nota = 85;  

// Ternario anidado para asignar la letra según la nota
let letra = (nota >= 90) ? "A" :    // Si >= 90 → "A"
            (nota >= 80) ? "B" :    // Si >= 80 → "B"
            (nota >= 70) ? "C" :    // Si >= 70 → "C"
            (nota >= 60) ? "D" : "F"; // Si >= 60 → "D", si no → "F"

console.log("Calificación:", letra);  // Muestra: "Calificación: B"
