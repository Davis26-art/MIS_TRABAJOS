// -----------------------------------------
// Ejercicio 50: Palíndromo
// -----------------------------------------
// Verifica si un texto o número es palíndromo.

let palabra = "radar"; // texto de entrada
let invertida = "";    // almacenará el texto al revés

// Recorre la palabra de atrás hacia adelante
for (let i = palabra.length - 1; i >= 0; i--) {
    invertida += palabra[i]; // agrega cada letra al nuevo string
}

// Compara original con invertida
if (palabra === invertida) {
    console.log(palabra, "es un palíndromo");
} else {
    console.log(palabra, "NO es un palíndromo");
}
