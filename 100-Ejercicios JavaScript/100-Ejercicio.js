// -----------------------------------------
// Ejercicio 100: Sistema de Autenticación
// -----------------------------------------
// Simula login con usuario y contraseña.

let usuarioGuardado = "admin"; // usuario correcto almacenado
let claveGuardada = "1234";    // contraseña correcta almacenada

function login(usuario, clave) {
    // Compara los datos ingresados con los guardados
    if (usuario === usuarioGuardado && clave === claveGuardada) {
        console.log("Acceso permitido"); // si ambos coinciden
    } else {
        console.log("Acceso denegado");  // si alguno falla
    }
}

// Pruebas del login
login("admin", "1234"); // acceso correcto
login("user", "pass");  // acceso incorrecto
