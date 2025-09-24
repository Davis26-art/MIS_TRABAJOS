// Ejercicio 4: Calculadora básica
console.log('Esta es una calculadora: ');

// Solicitar al usuario el tipo de operación y los números
var operador = prompt('Digita el calculo que vas a hacer (+, -, *, /): ');

// Convertir los valores ingresados a números
var numero1 = Number(prompt('Digita tu el primer número: '));
var numero2 = Number(prompt('Digita tu el segundo número: '));

// Realizar la operación según el operador ingresado
if (operador == '+') {
    var calculo_sum = numero1 + numero2;// Suma
    console.log(calculo_sum);

} else if (operador == '-') {
    var calculo_res = numero1 - numero2;// Resta
    console.log(calculo_res);

} else if (operador == '*') {
    var calculo_mult = numero1 * numero2;// Multiplicación
    console.log(calculo_mult);

} else if (operador == '/') {
    if (numero2 == 0) {// Validar división por cero
        console.log('No es posible dividir por 0.');// Mensaje de error
    } else {
        var calculo_div = numero1 / numero2;// División
        console.log(calculo_div);
    }

} else {
    console.log('Operación Invalida.');// Mensaje de error

}
