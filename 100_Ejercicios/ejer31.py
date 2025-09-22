#--------------------------------------------------
# Ejercicio 31: Calculadora con Resumen y Descuento
#--------------------------------------------------

# --- Clase ---
class Calculadora:
    def __init__(self):
        """
        Constructor de la clase Calculadora.
        Inicializa el historial como una lista vacía para almacenar todas las operaciones.
        """
        self.historial = []  # Lista donde se guardarán todas las operaciones

    def operar(self, num1, num2, operador):
        """
        Realiza la operación indicada entre num1 y num2 según el operador.
        Aplica un descuento del 10% si el resultado es mayor a 100.
        Guarda cada operación en el historial.
        """
        # Operaciones básicas según el operador
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            # Validación para no dividir entre cero
            resultado = num1 / num2 if num2 != 0 else "No se puede dividir entre 0"
        else:
            resultado = "Operador no válido"

        # Descuento del 10% si el resultado es un número y es mayor a 100
        if isinstance(resultado, (int, float)) and resultado > 100:
            resultado = resultado * 0.9  # Aplica 10% de descuento

        # Guardamos la operación en el historial como tupla
        self.historial.append((num1, operador, num2, resultado))
        return resultado

    def mostrar_historial(self):
        """
        Muestra todas las operaciones realizadas hasta el momento.
        """
        for op in self.historial:
            print(f"{op[0]} {op[1]} {op[2]} = {op[3]}")

    def mostrar_resumen(self):
        """
        Muestra un resumen con:
        - Total de operaciones realizadas
        - Último resultado obtenido
        """
        print("\n--- Resumen ---")
        print(f"Total de operaciones: {len(self.historial)}")
        if self.historial:
            print(f"Último resultado: {self.historial[-1][3]}")
        else:
            print("No hay operaciones registradas.")

# --- Programa Principal ---
# Creamos un objeto Calculadora para David y Camelo
calc_david = Calculadora()
calc_camelo = Calculadora()

while True:
    # Elegimos para quién se hará la operación
    persona = input("¿Quién usará la calculadora? (David/Camelo, o 'fin'): ").capitalize()
    if persona.lower() == "fin":
        break
    if persona not in ("David", "Camelo"):
        print("Nombre no válido. Elige David o Camelo.")
        continue

    # Pedimos al usuario los números y el operador
    num1 = float(input(f"Ingrese el primer número para {persona}: "))
    num2 = float(input(f"Ingrese el segundo número para {persona}: "))
    operador = input("Ingresa el operador (+, -, *, /): ")

    # Ejecutamos la operación y obtenemos el resultado
    if persona == "David":
        resultado = calc_david.operar(num1, num2, operador)
    else:
        resultado = calc_camelo.operar(num1, num2, operador)

    print(f"Resultado para {persona}: {resultado}")

    # Preguntamos si quiere seguir haciendo operaciones
    seguir = input("¿Quieres hacer otra operación? (si/no): ").lower()
    if seguir == "no":
        break

# Mostramos el historial completo y un resumen para ambos
print("\nHistorial de operaciones de David:")
calc_david.mostrar_historial()
calc_david.mostrar_resumen()

print("\nHistorial de operaciones de Camelo:")
calc_camelo.mostrar_historial()
calc_camelo.mostrar_resumen()
