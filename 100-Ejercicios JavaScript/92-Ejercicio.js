// -----------------------------------------
// Ejercicio 92: Generador de Tablas
// -----------------------------------------
// Genera la tabla de multiplicar de un número.

function tablaMultiplicar(n) {
    for (let i = 1; i <= 10; i++) {
        console.log(n, "x", i, "=", n * i); // imprime la multiplicación
    }
}

// Ejemplo de uso
tablaMultiplicar(6);
