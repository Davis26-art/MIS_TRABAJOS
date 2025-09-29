// -----------------------------------------
// Ejercicio 59: Números Perfectos
// -----------------------------------------
// Encuentra números perfectos hasta un límite.
// (Perfecto: suma de divisores = número, ej. 6)

let limite = 30;   // hasta dónde buscar

for (let num = 2; num <= limite; num++) {
    let sumaDiv = 0; // acumulador de divisores
    
    // buscamos divisores de 'num'
    for (let i = 1; i < num; i++) {
        if (num % i === 0) { // si i divide a num sin residuo
            sumaDiv += i;    // lo sumamos
        }
    }

    // comprobamos si es perfecto
    if (sumaDiv === num) {
        console.log(num, "es un número perfecto");
    }
}
