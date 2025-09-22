#--------------------------------------------------
# Ejercicio 71: Registro de Gastos por Categoría
#--------------------------------------------------

# --- Clase Gasto ---
class Gasto:
    def __init__(self):
        """
        Inicializa una lista vacía para almacenar los gastos.
        Cada gasto será una tupla: (nombre, valor, categoría)
        """
        self.gastos = []  # Lista de tuplas

    def agregar_gasto(self, nombre, valor, categoria):
        """
        Agrega un gasto a la lista.
        - nombre: descripción del gasto
        - valor: monto del gasto
        - categoria: categoría a la que pertenece
        """
        self.gastos.append((nombre, valor, categoria))

    def total_gastos(self):
        """
        Calcula el total de todos los gastos sumando los valores.
        """
        return sum(valor for _, valor, _ in self.gastos)

    def resumen_por_categoria(self):
        """
        Calcula el total de gastos por cada categoría.
        Retorna un diccionario: {categoría: total}
        """
        categorias = {}
        for _, valor, categoria in self.gastos:
            categorias[categoria] = categorias.get(categoria, 0) + valor
        return categorias

# --- Programa Principal ---
control = Gasto()  # Instancia de la clase para manejar los gastos

while True:
    nombre = input("Nombre del gasto (o 'fin'): ")

    # Condición de salida
    if nombre.lower() == "fin":
        break

    # Conversión de valor ingresado a float
    valor = float(input(f"Valor de {nombre}: "))

    # Capitaliza la categoría ingresada para uniformidad
    categoria = input(f"Categoría de {nombre}: ").capitalize()

    # Uso de variables David y Camelo como variables auxiliares sin afectar funcionalidad
    David = valor * 1  # Variable auxiliar, igual al valor ingresado
    Camelo = categoria  # Variable auxiliar, igual a la categoría ingresada

    # Agrega el gasto usando los valores originales (o las variables auxiliares)
    control.agregar_gasto(nombre, David, Camelo)

# --- Mostrar resumen ---
print("\nResumen por categorías:")
for cat, total in control.resumen_por_categoria().items():
    print(f"{cat}: ${total}")

print(f"Total: ${control.total_gastos()}")
