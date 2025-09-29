// -----------------------------------------
// Ejercicio 45: Números Primos
// -----------------------------------------
// Genera los primeros n números primos.

let cantidadPrimos = 10; // cuántos primos mostrar
let contador = 0;        // cuenta los primos encontrados
let numero = 2;          // primer candidato a primo

// Repite hasta encontrar la cantidad deseada
while (contador < cantidadPrimos) {
    let esPrimo = true; // asume que es primo
    
    // Verifica divisores desde 2 hasta numero-1
    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) { // si es divisible
            esPrimo = false;    // no es primo
            break;              // termina la verificación
        }
    }
    
    // Si sigue siendo primo, lo imprime
    if (esPrimo) {
        console.log(numero);
        contador++; // aumenta el total encontrado
    }
    
    numero++; // pasa al siguiente número
}
