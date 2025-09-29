// -----------------------------------------
// Ejercicio 83: Generador de Contraseñas
// -----------------------------------------
// Genera una contraseña aleatoria de longitud n.

// Función que genera una contraseña
function generarPassword(longitud) {
    // Conjunto de caracteres que se pueden usar
    let caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let password = ""; // inicializamos la contraseña vacía

    // Repetimos tantas veces como indique la longitud
    for (let i = 0; i < longitud; i++) {
        // Math.random() → número aleatorio entre 0 y 1
        // Math.random() * caracteres.length → entre 0 y el número de caracteres
        // Math.floor() → redondea hacia abajo para obtener un índice válido
        let random = Math.floor(Math.random() * caracteres.length);

        // Añadimos el carácter seleccionado al password
        password += caracteres[random];
    }

    // Devolvemos la contraseña generada
    return password;
}

// Probamos la función generando una contraseña de 8 caracteres
console.log("Contraseña generada:", generarPassword(8));
