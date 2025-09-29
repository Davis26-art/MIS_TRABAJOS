// -----------------------------------------
// Ejercicio 93: Validador de Tarjeta (Luhn)
// -----------------------------------------
// Verifica si un número de tarjeta es válido.

function validarTarjeta(numero) {
    // Convierte el número a array de dígitos
    let digitos = numero.toString().split("").map(Number);
    let suma = 0;

    // Recorre los dígitos de derecha a izquierda
    for (let i = digitos.length - 1; i >= 0; i--) {
        let num = digitos[i];
        // Doble cada segundo dígito desde la derecha
        if ((digitos.length - i) % 2 === 0) {
            num *= 2;
            if (num > 9) num -= 9; // si es mayor que 9, restar 9
        }
        suma += num;
    }

    // Si la suma es divisible entre 10, la tarjeta es válida
    return suma % 10 === 0;
}

// Ejemplos de uso
console.log("Tarjeta válida?", validarTarjeta(4539578763621486)); // true
console.log("Tarjeta válida?", validarTarjeta(1234567890123456)); // false
