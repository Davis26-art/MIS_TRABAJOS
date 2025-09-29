// -----------------------------------------
// Ejercicio 23: Estación del Año
// -----------------------------------------

// Número del mes (1-12)
let mes = 9;

// Switch según el mes
switch (mes) {
    case 12: case 1: case 2:      // diciembre, enero, febrero
        console.log("Invierno");
        break;
    case 3: case 4: case 5:       // marzo, abril, mayo
        console.log("Primavera");
        break;
    case 6: case 7: case 8:       // junio, julio, agosto
        console.log("Verano");
        break;
    case 9: case 10: case 11:     // septiembre, octubre, noviembre
        console.log("Otoño");
        break;
    default:
        console.log("Mes inválido"); // fuera de 1-12
}
