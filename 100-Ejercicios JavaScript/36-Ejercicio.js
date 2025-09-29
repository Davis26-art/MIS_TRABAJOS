// -----------------------------------------
// Ejercicio 36: Clasificador de Triángulos
// -----------------------------------------

// Tres lados del triángulo
let lado1 = 5, lado2 = 5, lado3 = 5;

// Switch con condición lógica
switch (true) {
    case (lado1 === lado2 && lado2 === lado3): // todos iguales
        console.log("Equilátero");
        break;
    case (lado1 === lado2 || lado2 === lado3 || lado1 === lado3): // solo 2 iguales
        console.log("Isósceles");
        break;
    default: // todos diferentes
        console.log("Escaleno");
}
