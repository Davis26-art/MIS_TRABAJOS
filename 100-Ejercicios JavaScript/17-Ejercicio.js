// -----------------------------------------
// Ejercicio 17: MCD y MCM
// -----------------------------------------

// Dos números de ejemplo
let x = 12, y = 18;

// Función para calcular MCD con Euclides
function mcd(a, b) {
    while (b !== 0) {       // se repite mientras b no sea 0
        let temp = b;       // guarda b
        b = a % b;          // b toma el residuo
        a = temp;           // a toma el valor anterior de b
    }
    return a;               // cuando b=0, a es el MCD
}

// Calcula el MCD
let resultadoMCD = mcd(x, y);

// MCM se obtiene con la fórmula: (x * y) / MCD
let resultadoMCM = (x * y) / resultadoMCD;

// Imprime los resultados
console.log("MCD:", resultadoMCD);
console.log("MCM:", resultadoMCM);
