// -----------------------------------------
// Ejercicio 103: Signo de Número
// -----------------------------------------

let numero = -5;  
// Definimos el número que queremos evaluar

let signo = (numero > 0) ? "Positivo" : (numero < 0 ? "Negativo" : "Cero");  
// Operador ternario anidado:
// Si numero > 0 → "Positivo"
// Si no, evaluamos si numero < 0 → "Negativo"
// Si ninguna de las dos condiciones se cumple → "Cero"

console.log(numero, "es", signo);  
// Muestra en consola: "-5 es Negativo"
