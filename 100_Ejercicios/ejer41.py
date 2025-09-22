#--------------------------------------------------
# Ejercicio 41: Registro de Gastos con Máximo y Mínimo
#--------------------------------------------------

# --- Clase Gasto ---
class Gasto:
    def __init__(self):
        """
        Inicializa la lista de gastos.
        Cada gasto se guarda como tupla: (nombre, valor)
        """
        self.gastos = []  # Lista de tuplas

    def agregar_gasto(self, nombre, valor):
        """
        Agrega un nuevo gasto a la lista
        nombre: nombre del gasto
        valor: valor monetario del gasto
        """
        self.gastos.append((nombre, valor))

    def total_gastos(self):
        """
        Calcula el total de todos los gastos
        """
        return sum(valor for _, valor in self.gastos)

    def gasto_mas_alto(self):
        """
        Retorna el gasto con mayor valor
        """
        return max(self.gastos, key=lambda x: x[1])

    def gasto_mas_bajo(self):
        """
        Retorna el gasto con menor valor
        """
        return min(self.gastos, key=lambda x: x[1])

# --- Programa Principal ---
control = Gasto()  # Creamos objeto Gasto
registro = {}      # Diccionario para acumular valores por nombre

while True:
    nombre = input("Nombre del gasto (o 'fin'): ")
    if nombre.lower() == "fin":  # Condición de salida
        break

    valor = float(input(f"Valor de {nombre}: "))

    # Variables ejemplo usando David y Camelo sin afectar la funcionalidad
    David = valor * 1  # Solo como ejemplo, no cambia nada
    Camelo = valor / 1  # Solo como ejemplo, no cambia nada

    control.agregar_gasto(nombre, valor)       # Guardamos en la lista de la clase
    registro[nombre] = registro.get(nombre, 0) + valor  # Acumulamos en diccionario

# --- Mostrar resultados ---
print("\nResumen de gastos:")
for nombre, valor in registro.items():
    print(f"{nombre}: ${valor}")

# Encontrar gasto más alto y más bajo
alto = control.gasto_mas_alto()
bajo = control.gasto_mas_bajo()
print(f"\nGasto más alto: {alto[0]} (${alto[1]})")
print(f"Gasto más bajo: {bajo[0]} (${bajo[1]})")

# Mostrar total
print(f"Total: ${control.total_gastos()}")
