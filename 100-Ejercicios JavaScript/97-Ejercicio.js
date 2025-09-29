// -----------------------------------------
// Ejercicio 97: Calculadora Científica
// -----------------------------------------
// Funciones matemáticas básicas usando Math

// Función para calcular la raíz cuadrada
function raizCuadrada(n) { 
    return Math.sqrt(n); // Math.sqrt(x) devuelve la raíz cuadrada de x
}

// Función para calcular la potencia
function potencia(base, exp) { 
    return Math.pow(base, exp); // Math.pow(a, b) devuelve a elevado a la b
}

// Función para calcular el logaritmo natural (base e)
function logaritmo(n) { 
    return Math.log(n); // Math.log(x) devuelve el logaritmo natural de x
}

// Función para calcular el seno de un ángulo en radianes
function seno(n) { 
    return Math.sin(n); // Math.sin(x) devuelve el seno de x (en radianes)
}

// Pruebas de las funciones
console.log("Raíz:", raizCuadrada(16));          // 4
console.log("Potencia:", potencia(2, 5));        // 32
console.log("Logaritmo:", logaritmo(10));        // ~2.302
console.log("Seno:", seno(Math.PI / 2));         // 1
