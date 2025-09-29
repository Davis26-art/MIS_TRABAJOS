// -----------------------------------------
// Ejercicio 30: Piedra, Papel o Tijera
// -----------------------------------------

// Elecciones de los jugadores
let jugador1 = "piedra";
let jugador2 = "tijera";

// Combina jugadas en un string "jugador1-jugador2"
switch (jugador1 + "-" + jugador2) {
    // Casos donde gana jugador 1
    case "piedra-tijera":
    case "tijera-papel":
    case "papel-piedra":
        console.log("Jugador 1 gana");
        break;

    // Casos donde gana jugador 2
    case "tijera-piedra":
    case "papel-tijera":
    case "piedra-papel":
        console.log("Jugador 2 gana");
        break;

    // Si son iguales → empate
    default:
        console.log("Empate");
}
