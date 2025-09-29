// -----------------------------------------
// Ejercicio 99: Simulador de Dados
// -----------------------------------------
// Lanza un dado de 6 caras

function lanzarDado() {
    // Math.random() genera un número decimal aleatorio entre 0 y 1 (no incluye 1)
    // Multiplicamos por 6 para obtener un rango entre 0 y 5.999...
    // Math.floor() redondea hacia abajo, dando un entero entre 0 y 5
    // +1 ajusta el rango a 1-6, como un dado real
    return Math.floor(Math.random() * 6) + 1;
}

console.log("Resultado del dado:", lanzarDado());
