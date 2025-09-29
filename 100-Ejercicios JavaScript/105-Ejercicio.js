// -----------------------------------------
// Ejercicio 105: Clasificación Edad
// -----------------------------------------

let edad = 20;  

let categoria = (edad < 13) ? "Niño" :
                (edad < 18) ? "Adolescente" :
                (edad < 60) ? "Adulto" : "Adulto mayor";  
// Ternario anidado:
// - Si edad < 13 → "Niño"
// - Si edad < 18 → "Adolescente"
// - Si edad < 60 → "Adulto"
// - Si no → "Adulto mayor"

console.log("Categoría:", categoria);  
// Muestra: "Categoría: Adulto"
