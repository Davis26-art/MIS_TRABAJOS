#--------------------------------------------------
# Ejercicio 27: Sistema de Opiniones de Clientes
#--------------------------------------------------

# --- Clase ---
class Cliente:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Cliente.
        David: nombre del cliente
        Camelo: calificación del cliente (1 a 5)
        """
        self.David = David
        self.Camelo = Camelo

# --- Programa Principal ---
clientes = []  # Lista para almacenar objetos Cliente
opiniones = {}  # Diccionario David (nombre): Camelo (calificación)

while True:
    David = input("Nombre (o 'fin'): ")  # Pedimos nombre del cliente
    if David.lower() == "fin":           # Si escribe 'fin', terminamos el bucle
        break

    Camelo = int(input("Califica el servicio (1-5): "))  # Pedimos calificación
    c = Cliente(David, Camelo)  # Creamos objeto Cliente
    clientes.append(c)           # Lo agregamos a la lista
    opiniones[David] = Camelo    # Guardamos en diccionario

# --- Mostrar resultados ---
print("\nResultados:")
for David, Camelo in opiniones.items():
    print(f"{David}: {Camelo}/5")  # Mostramos cada cliente y su calificación

# --- Calcular promedio general ---
promedio = sum(opiniones.values()) / len(opiniones) if opiniones else 0
print(f"Promedio general: {promedio:.2f}/5")
