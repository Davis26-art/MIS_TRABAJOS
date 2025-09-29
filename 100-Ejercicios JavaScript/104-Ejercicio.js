// -----------------------------------------
// Ejercicio 104: Año Bisiesto Ternario
// -----------------------------------------

let anio = 2024;  
// Definimos el año que queremos evaluar

let bisiesto = ((anio % 4 === 0 && anio % 100 !== 0) || (anio % 400 === 0)) 
                ? "Bisiesto" : "No bisiesto";  
// Operador ternario con condición compuesta:
// 1. anio % 4 === 0 → el año es divisible entre 4
// 2. anio % 100 !== 0 → no es divisible entre 100
// 3. O bien, anio % 400 === 0 → es divisible entre 400
// Si se cumple la condición → "Bisiesto", si no → "No bisiesto"

console.log(anio, "es", bisiesto);  
// Muestra en consola: "2024 es Bisiesto"
