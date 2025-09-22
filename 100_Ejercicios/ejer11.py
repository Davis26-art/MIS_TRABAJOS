#--------------------------------------------------
# Ejercicio 11: Registro de Gastos
#--------------------------------------------------

# --- Clase ---
class Gasto:
    def __init__(self):
        """
        Constructor de la clase Gasto.
        Crea una lista vacía llamada self.David donde se guardarán
        los gastos en forma de tuplas (nombre, valor).
        """
        self.David = []  # Lista de tuplas (nombre, valor)

    def agregar_gasto(self, nombre, valor):
        """
        Agrega un nuevo gasto a la lista self.David.
        Cada gasto se almacena como una tupla: (nombre, valor).
        """
        self.David.append((nombre, valor))

    def total_gastos(self):
        """
        Calcula el total de todos los gastos sumando los valores.
        Recorre la lista self.David y extrae el valor de cada tupla.
        """
        return sum(valor for _, valor in self.David)

# --- Programa Principal ---
Camelo = Gasto()  # Se crea un objeto de la clase Gasto llamado Camelo
registro = {}  # Diccionario para guardar el total por cada nombre de gasto

while True:
    nombre = input("Nombre del gasto (o 'fin'): ")
    if nombre.lower() == "fin":  # Si el usuario escribe "fin", termina el bucle
        break

    valor = float(input(f"Valor de {nombre}: "))
    Camelo.agregar_gasto(nombre, valor)  # Guardamos el gasto en la lista de Camelo
    # Si el nombre ya existe en el diccionario, sumamos al total. Si no, lo creamos.
    registro[nombre] = registro.get(nombre, 0) + valor

# Cuando el ciclo termina, mostramos el resumen
print("\nResumen de gastos:")
for nombre, valor in registro.items():
    print(f"{nombre}: ${valor}")  # Muestra el total gastado en cada concepto

# Mostramos el total general usando el método total_gastos
print(f"Total: ${Camelo.total_gastos()}")
