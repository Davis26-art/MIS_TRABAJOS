// -----------------------------------------
// Ejercicio 84: Validación de Email
// -----------------------------------------
// Verifica si el email tiene formato válido

function validarEmail(email) {
    // includes("@") → verifica si hay una arroba
    // includes(".") → verifica si hay un punto
    // Si ambos existen, consideramos el email válido
    if (email.includes("@") && email.includes(".")) {
        console.log(email, "es válido");
    } else {
        console.log(email, "NO es válido");
    }
}

// Probamos la función con dos ejemplos
validarEmail("correo@test.com"); // válido
validarEmail("correo@");          // no válido
