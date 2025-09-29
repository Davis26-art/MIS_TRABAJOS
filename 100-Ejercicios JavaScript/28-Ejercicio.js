// -----------------------------------------
// Ejercicio 28: Calculadora de Salario
// -----------------------------------------

// Horas trabajadas
let horas = 45;

// Tipo de empleado
let tipo = "normal"; // "normal" o "extra"

// Variable para el salario
let salario;

// Switch según el tipo de empleado
switch (tipo) {
    case "normal":                 // pago estándar
        salario = horas * 10;      // $10 por hora
        break;
    case "extra":                  // pago con horas extra
        salario = horas * 15;      // $15 por hora
        break;
    default:                       // tipo inválido
        salario = 0;
}

// Imprime el salario calculado
console.log("Salario total:", salario);
