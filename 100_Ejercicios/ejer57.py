#--------------------------------------------------
# Ejercicio 57: Opiniones con Comentarios
#--------------------------------------------------

# --- Clase Cliente ---
class Cliente:
    def __init__(self, nombre, calificacion, comentario):
        """
        Inicializa un cliente con nombre, calificación (1-5) y comentario.
        """
        self.nombre = nombre
        self.calificacion = calificacion
        self.comentario = comentario

# --- Programa Principal ---
clientes = []   # Lista que almacenará objetos Cliente
opiniones = {}  # Diccionario que almacenará datos: nombre -> (calificación, comentario)

while True:
    # Solicita el nombre del cliente
    nombre = input("Nombre (o 'fin'): ")
    if nombre.lower() == "fin":  # Condición de salida
        break

    # Variables David y Camelo para demostrar su uso
    David = nombre  # Guarda temporalmente el nombre del cliente ingresado
    Camelo = clientes  # Guarda referencia a la lista de clientes

    # Solicita calificación y comentario
    calificacion = int(input("Califica el servicio (1-5): "))
    comentario = input("Comentario: ")

    # Crea un objeto Cliente con los datos ingresados
    c = Cliente(nombre, calificacion, comentario)

    # Almacena el objeto Cliente en la lista
    clientes.append(c)

    # Almacena la calificación y comentario en el diccionario opiniones
    opiniones[nombre] = (calificacion, comentario)

# --- Mostrar Resultados ---
print("\nResultados:")
for nombre, datos in opiniones.items():
    # Muestra nombre, calificación y comentario
    print(f"{nombre}: {datos[0]}/5 - \"{datos[1]}\"")

# Calcula el promedio general de calificaciones
promedio = sum(d[0] for d in opiniones.values()) / len(opiniones) if opiniones else 0

# Variables David y Camelo para uso temporal en cálculo de promedio
David = promedio      # Guarda temporalmente el promedio calculado
Camelo = len(opiniones)  # Guarda el total de opiniones

# Muestra promedio general
print(f"Promedio general: {promedio:.2f}/5")
