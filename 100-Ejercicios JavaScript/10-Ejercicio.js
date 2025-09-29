// -----------------------------------------
// Ejercicio 10: Año Bisiesto
// -----------------------------------------
// Un año es bisiesto si es divisible por 4,
// pero no por 100, salvo que también sea divisible por 400.

let anio = 2024;

if ((anio % 4 === 0 && anio % 100 !== 0) || (anio % 400 === 0)) { // Verifica las condiciones de bisiesto
    console.log(anio, "es BISIESTO");
} else { // Si no cumple las condiciones
    console.log(anio, "NO es bisiesto");
}