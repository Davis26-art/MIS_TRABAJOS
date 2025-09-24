// Ejercicio 6: Evaluar la temperatura y proporcionar un mensaje adecuado
const prompt = require("prompt-sync")(); 

let temperatura = Number(prompt('Digita la temperatura actual: ')); // Convertir el valor ingresado a número

// Evaluar la temperatura y proporcionar un mensaje adecuado
if (temperatura >= 30) {
    console.log('La temperatura esta muy alta, hace demasido calor....')
} else if (temperatura <= 20) {
    console.log('La temperatura esta muy baja, hace demasiado frio.... ')
} else {
    console.log('Vamos a morir de Hipotermia.....')
}