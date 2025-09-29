// -----------------------------------------
// Ejercicio 3: Mayor de Tres Números
// -----------------------------------------
// Usa if-else para encontrar el mayor de 3.

let a = 12, b = 25, c = 18;

if (a > b && a > c) { // Si 'a' es mayor que 'b' y 'c'
    console.log("El mayor es:", a);
} else if (b > c) { // Si 'b' es mayor que 'c'
    console.log("El mayor es:", b);
} else { // Si no, 'c' es el mayor
    console.log("El mayor es:", c);
}
