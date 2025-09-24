const prompt = require("prompt-sync")(); // Importar prompt-sync para entrada de usuario

/** Ejercicio 1 For */
for (let i = 0; i < 3; i++) {// Repetir 3 veces
  console.log("Hola mundo");// Imprimir "Hola mundo"
}


/** Ejercicio 2 For */
let frutas = ["manzana", "banana", "pera"];// Array de frutas

for (let i = 0; i < frutas.length; i++) {// Iterar sobre cada fruta en el array
  console.log(frutas[i]);// Imprimir el valor de cada fruta
}


/** Ejercicio 3 For */
for (let i = 1; i <= 5; i++) {// Contar de 1 a 5
  console.log(i);// Imprimir el valor de i
}


/** Ejercicio 4 For */
for (let i = 5; i >= 1; i--) {// Contar de 5 a 1
  console.log(i);// Imprimir el valor de i
}


/** Ejercicio 5 For*/
for (let i = 1; i <= 10; i++) {// Contar de 1 a 10
  if (i % 2 !== 0) {
    console.log(i);// Imprimir solo los números impares
  }
  if (i % 2 === 0) {
    console.log(i);// Imprimir solo los números pares
  }
}
