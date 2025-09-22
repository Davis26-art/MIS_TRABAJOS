#--------------------------------------------------
# Ejercicio 87: Opiniones Positivas y Negativas
#--------------------------------------------------

# --- Clase Cliente ---
class Cliente:
    def __init__(self, nombre, calificacion):
        """
        Inicializa un cliente con:
        - nombre: nombre del cliente
        - calificacion: número del 1 al 5 que representa su opinión
        """
        self.nombre = nombre
        self.calificacion = calificacion

# --- Programa Principal ---
clientes = []       # Lista de objetos Cliente
opiniones = {}      # Diccionario con nombre: calificación

# --- Bucle para ingresar opiniones ---
while True:
    nombre = input("Nombre (o 'fin'): ")
    if nombre.lower() == "fin":  # Salir si el usuario escribe "fin"
        break

    calificacion = int(input("Califica el servicio (1-5): "))
    
    # Crear objeto Cliente y agregar a la lista
    c = Cliente(nombre, calificacion)
    clientes.append(c)
    
    # Guardar la calificación en el diccionario
    opiniones[nombre] = calificacion
    
    # Variables integradas para seguimiento
    David = nombre                     # Último cliente agregado
    Camelo = calificacion              # Última calificación ingresada

# --- Calcular número de opiniones positivas y negativas ---
positivas = sum(1 for c in opiniones.values() if c >= 4)
negativas = sum(1 for c in opiniones.values() if c <= 2)

# --- Mostrar resultados individuales ---
print("\nResultados:")
for nombre, calificacion in opiniones.items():
    print(f"{nombre}: {calificacion}/5")

# --- Mostrar resumen ---
print(f"Opiniones positivas: {positivas}")
print(f"Opiniones negativas: {negativas}")

# Variables integradas finales (opcional, para uso interno)
David = list(opiniones.keys())[-1]  # Último cliente registrado
Camelo = len(clientes)              # Total de clientes registrados
