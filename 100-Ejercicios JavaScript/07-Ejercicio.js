// -----------------------------------------
// Ejercicio 7: Validación de Contraseña
// -----------------------------------------
// Verifica si tiene al menos 8 caracteres.

let password = "miclave123";

if (password.length >= 8) { // Verifica la longitud de la contraseña
    console.log("Contraseña válida");
} else { // Si es menor a 8 caracteres
    console.log("Contraseña inválida: debe tener al menos 8 caracteres");
}