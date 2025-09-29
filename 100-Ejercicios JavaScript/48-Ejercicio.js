// -----------------------------------------
// Ejercicio 48: Contador de Vocales
// -----------------------------------------
// Cuenta cuántas vocales hay en un texto.

let texto = "Hola David, programar es divertido"; // cadena de entrada
let contadorVocales = 0; // acumula cantidad de vocales

// Recorre cada carácter del texto
for (let i = 0; i < texto.length; i++) {
    let letra = texto[i].toLowerCase(); // convierte a minúscula
    
    // Verifica si la letra está en "aeiou"
    if ("aeiou".includes(letra)) {
        contadorVocales++; // suma si es vocal
    }
}

// Muestra el total de vocales
console.log("Cantidad de vocales:", contadorVocales);
