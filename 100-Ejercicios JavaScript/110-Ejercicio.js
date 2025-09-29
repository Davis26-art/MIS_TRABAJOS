// -----------------------------------------
// Ejercicio 110: Estado de Agua
// -----------------------------------------

let temp = 50;  // Temperatura en grados Celsius

// Clasificación con ternarios encadenados
let estado = (temp <= 0) ? "Sólido" :       // 0°C o menos → hielo
             (temp < 100) ? "Líquido" :    // Entre 1 y 99°C → agua líquida
             "Gaseoso";                    // 100°C o más → vapor

console.log("A", temp, "°C el agua está en estado:", estado);
// Muestra: "A 50 °C el agua está en estado: Líquido"
