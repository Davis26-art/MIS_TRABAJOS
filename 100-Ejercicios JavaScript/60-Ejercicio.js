// -----------------------------------------
// Ejercicio 60: Criba de Eratóstenes
// -----------------------------------------
// Encuentra todos los primos hasta n.

let max = 50;  
let esPrimo = new Array(max + 1).fill(true); // asumimos que todos son primos

esPrimo[0] = esPrimo[1] = false; // 0 y 1 no son primos

// eliminamos múltiplos de cada primo
for (let i = 2; i * i <= max; i++) {
    if (esPrimo[i]) { // si sigue marcado como primo
        for (let j = i * i; j <= max; j += i) {
            esPrimo[j] = false; // múltiplos no son primos
        }
    }
}

// mostramos todos los que quedaron como primos
console.log("Primos hasta", max, ":");
for (let i = 2; i <= max; i++) {
    if (esPrimo[i]) console.log(i);
}
