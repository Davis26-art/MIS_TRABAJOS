// -----------------------------------------
// Ejercicio 31: Calculadora de Impuestos
// -----------------------------------------

// Ingresos del usuario
let ingresos = 3500;
let impuesto;

// Switch con true para evaluar rangos
switch (true) {
    case (ingresos <= 1000):       // hasta 1000 → 5%
        impuesto = ingresos * 0.05;
        break;
    case (ingresos <= 5000):       // 1001-5000 → 10%
        impuesto = ingresos * 0.10;
        break;
    default:                       // más de 5000 → 15%
        impuesto = ingresos * 0.15;
}

// Imprime el impuesto calculado
console.log("Impuesto a pagar:", impuesto);
