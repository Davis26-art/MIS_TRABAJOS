// Ejercicio 8: Uso de condicionales y operadores ternarios 
const prompt = require("prompt-sync")(); // Importar prompt-sync para entrada de usuario

/** Ejercicio 1 */
// Pedir al usuario un número y determinar si es positivo, negativo o cero
let num = Number(prompt('Digita un número: '))

if (num > 0) {// Validar si el número es positivo
  console.log('Este número es positivo. ');

} else if (num < 0) {// Validar si el número es negativo
  console.log('Este número es negativo. ');

} else {// Validar si el número es cero
  console.log('Este número es 0.');

}
// Usar operador ternario para determinar si el número es positivo, negativo o cero
let Numero_tipo = num > 0 ? 'Este número es positivo. ' : (num < 0 ? 'Este número es negativo. ' : 'Este número es 0.');
console.log(Numero_tipo);



/** Ejercicio 2 */
// Pedir al usuario su nombre y verificar si está vacío
let nombre = prompt('Digita tu nombre: ')

if (nombre === '') {// Validar si el nombre está vacío
  console.log('El nombre está vacio. ');
} else {// Si el nombre no está vacío, mostrar el nombre ingresado
  console.log('Nombre ingresado: ', nombre);
}
// Usar operador ternario para verificar si el nombre está vacío
let Validar_nombre = nombre === '' ? 'El nombre está vacio. ' : `Nombre ingresado: ${nombre}`;
console.log(Validar_nombre);




/** Ejercicio 3 */
let temperatura = 22;// Temperatura en grados Celsius

if (temperatura >= 20 && temperatura <= 25) {// Validar si la temperatura está en el rango ideal
  console.log("Temperatura ideal");
} else {// Si la temperatura está fuera del rango ideal
  console.log("Temperatura fuera de rango");
}
// Usar operador ternario para verificar si la temperatura está en el rango ideal
console.log((temperatura >= 20 && temperatura <= 25) ? "Temperatura ideal" : "Temperatura fuera de rango");



/** Ejercicio 4 */
let contraseña = "abc123";// Contraseña ingresada por el usuario

if (contraseña.length >= 8) {// Validar si la contraseña tiene al menos 8 caracteres
  console.log("Contraseña segura");
} else {// Si la contraseña tiene menos de 8 caracteres
  console.log("Contraseña débil");
}
// Usar operador ternario para verificar la seguridad de la contraseña
console.log(contraseña.length >= 8 ? "Contraseña segura" : "Contraseña débil");



/** Ejercicio 5 */
let numero = 10;// Número ingresado por el usuario

if (numero % 5 === 0) {// Validar si el número es divisible por 5
  console.log("Es divisible por 5");
} else {// Si el número no es divisible por 5
  console.log("No es divisible por 5");
}
// Usar operador ternario para verificar si el número es divisible por 5
console.log(numero % 5 === 0 ? "Es divisible por 5" : "No es divisible por 5");
