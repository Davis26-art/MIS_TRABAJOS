// -----------------------------------------
// Ejercicio 24: Calculadora de Figuras
// -----------------------------------------

// Figura a calcular
let figura = "círculo";
let area;

// Switch según la figura
switch (figura) {
    case "círculo":              // área = π * r²
        let radio = 5;
        area = Math.PI * (radio ** 2);
        console.log("Área del círculo:", area);
        break;
    case "cuadrado":             // área = lado * lado
        let lado = 4;
        area = lado * lado;
        console.log("Área del cuadrado:", area);
        break;
    case "rectángulo":           // área = base * altura
        let base = 6, alturaRect = 3;
        area = base * alturaRect;
        console.log("Área del rectángulo:", area);
        break;
    default:                     // si no coincide
        console.log("Figura no válida");
}
