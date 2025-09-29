// -----------------------------------------
// Ejercicio 94: Cifrado César
// -----------------------------------------
// Desplaza letras n posiciones en el alfabeto.

function cifradoCesar(texto, desplazamiento) {
    let resultado = "";
    
    for (let i = 0; i < texto.length; i++) {
        let char = texto[i];
        
        if (/[a-z]/.test(char)) {
            // Para minúsculas: 'a' = 97 en ASCII
            let codigo = (char.charCodeAt(0) - 97 + desplazamiento) % 26 + 97;
            resultado += String.fromCharCode(codigo);
        } else if (/[A-Z]/.test(char)) {
            // Para mayúsculas: 'A' = 65 en ASCII
            let codigo = (char.charCodeAt(0) - 65 + desplazamiento) % 26 + 65;
            resultado += String.fromCharCode(codigo);
        } else {
            // Mantiene caracteres no alfabéticos sin cambios
            resultado += char;
        }
    }
    
    return resultado;
}

console.log("Cifrado:", cifradoCesar("Hola Mundo", 3)); // "Krod Pxqgr"
