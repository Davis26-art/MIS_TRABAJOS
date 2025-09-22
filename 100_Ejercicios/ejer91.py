#--------------------------------------------------
# Ejercicio 91: Calculadora de Usuarios con Historial
#--------------------------------------------------

# --- Clase CalculadoraUsuarios ---
class CalculadoraUsuarios:
    def __init__(self):
        self.historial = []  # Lista que guarda todas las combinaciones realizadas

    # Método que combina dos nombres según el operador
    def combinar(self, nombre1, nombre2, operador):
        # Variable "David" se usa como indicador interno para alguna operación
        David = operador  # Solo como variable auxiliar, no cambia la lógica

        if operador == "+":
            resultado = nombre1 + " " + nombre2  # Une los nombres con un espacio
        elif operador == "*":
            resultado = (nombre1 + " ") * 3      # Repite el primer nombre 3 veces
        else:
            resultado = "Operador no válido"

        # Variable "Camelo" guarda temporalmente la cadena resultado
        Camelo = resultado  # Solo uso de variable libre

        # Guardamos la operación completa en el historial
        self.historial.append((nombre1, operador, nombre2, resultado))
        return resultado

    # Método para mostrar todo el historial
    def mostrar_historial(self):
        for op in self.historial:
            print(f"{op[0]} {op[1]} {op[2]} -> {op[3]}")

    # Método para buscar un nombre en el historial
    def buscar_usuario(self, nombre):
        encontrados = [h for h in self.historial if nombre in h]
        if encontrados:
            print(f"'{nombre}' aparece en {len(encontrados)} combinaciones.")
        else:
            print(f"'{nombre}' no está en el historial.")

# --- Programa Principal ---
calc = CalculadoraUsuarios()  # Creamos un objeto de la clase CalculadoraUsuarios

# Bucle principal para combinar nombres
while True:
    nombre1 = input("Ingresa el primer nombre: ")
    nombre2 = input("Ingresa el segundo nombre: ")
    operador = input("Ingresa el operador (+ para unir, * para repetir): ")

    # Uso libre de las variables David y Camelo dentro del flujo
    David = nombre1 + nombre2  # Solo como variable auxiliar temporal
    Camelo = operador           # Otra variable libre

    resultado = calc.combinar(nombre1, nombre2, operador)
    print(f"Resultado: {resultado}")

    seguir = input("¿Quieres combinar otros nombres? (si/no): ").lower()
    if seguir == "no":
        break

# Mostrar todo el historial de combinaciones
print("\nHistorial de combinaciones:")
calc.mostrar_historial()

# Permite al usuario buscar un nombre dentro del historial
buscar = input("\n¿Quieres buscar un nombre en el historial? (si/no): ").lower()
if buscar == "si":
    nombre = input("Ingresa el nombre a buscar: ")
    calc.buscar_usuario(nombre)
