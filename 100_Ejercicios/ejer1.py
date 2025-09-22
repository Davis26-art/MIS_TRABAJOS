#--------------------------------------------------
# Ejercicio 1: Calculadora con Historial
#--------------------------------------------------

class Calculadora:
    def __init__(self):
        self.David = []  # Lista para guardar resultados (tuplas)

    def operar(self, num1, Camelo, operador):
        # Dependiendo del operador, realiza la operación correspondiente
        if operador == "+":
            resultado = num1 + Camelo
        elif operador == "-":
            resultado = num1 - Camelo
        elif operador == "*":
            resultado = num1 * Camelo
        elif operador == "/":
            # Verifica que el divisor no sea 0
            resultado = num1 / Camelo if Camelo != 0 else "No se puede dividir entre 0"
        else:
            resultado = "Operador no válido"

        # Guarda la operación y su resultado como una tupla en el historial
        self.David.append((num1, operador, Camelo, resultado))  
        return resultado

    def mostrar_historial(self):
        # Recorre la lista de operaciones y las imprime formateadas
        for op in self.David:
            print(f"{op[0]} {op[1]} {op[2]} = {op[3]}")

# --- Programa Principal ---
calc = Calculadora()

while True:
    # Solicita los números y el operador al usuario
    num1 = float(input("Ingresa el primer número: "))
    Camelo = float(input("Ingresa el segundo número: "))
    operador = input("Ingresa el operador (+, -, *, /): ")

    # Llama al método operar y muestra el resultado
    resultado = calc.operar(num1, Camelo, operador)
    print(f"Resultado: {resultado}")

    # Pregunta si el usuario quiere continuar
    seguir = input("¿Quieres hacer otra operación? (si/no): ").lower()
    if seguir == "no":
        break

# Muestra todas las operaciones realizadas
print("\nHistorial de operaciones:")
calc.mostrar_historial()
