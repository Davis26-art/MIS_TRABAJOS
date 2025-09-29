// -----------------------------------------
// Ejercicio 37: Calculadora de Calorías
// -----------------------------------------

let actividad = "correr"; // tipo de actividad
let tiempo = 30;          // duración en minutos
let calorias;

// Selección según actividad
switch (actividad) {
    case "correr":                  // correr quema 10 cal/min
        calorias = tiempo * 10;
        break;
    case "nadar":                   // nadar quema 8 cal/min
        calorias = tiempo * 8;
        break;
    case "caminar":                 // caminar quema 4 cal/min
        calorias = tiempo * 4;
        break;
    default:                        // actividad no válida
        calorias = 0;
}

// Resultado final
console.log("Calorías quemadas:", calorias);
