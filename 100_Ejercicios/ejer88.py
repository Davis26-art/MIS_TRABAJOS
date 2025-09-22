#--------------------------------------------------
# Ejercicio 88: Registro de Mascotas
#--------------------------------------------------

# --- Clase Mascota ---
class Mascota:
    def __init__(self, nombre, especie):
        """
        Inicializa una mascota con:
        - nombre: nombre de la mascota
        - especie: tipo de animal (perro, gato, etc.)
        """
        self.nombre = nombre
        self.especie = especie

# --- Programa Principal ---
mascotas = []   # Lista de objetos Mascota
registro = {}   # Diccionario con nombre: especie para búsquedas rápidas

# --- Bucle principal de opciones ---
while True:
    opcion = input("\n1. Registrar Mascota\n2. Buscar Mascota\n3. Mostrar Todas\n0. Salir\nOpción: ")

    # --- Opción 1: Registrar nueva mascota ---
    if opcion == "1":
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        m = Mascota(nombre, especie)  # Crear objeto Mascota
        mascotas.append(m)             # Agregar a la lista de objetos
        registro[nombre] = especie    # Guardar en diccionario para búsquedas rápidas

        # Variables integradas David y Camelo
        David = nombre    # Nombre de la última mascota registrada
        Camelo = especie  # Especie de la última mascota registrada

    # --- Opción 2: Buscar mascota por nombre ---
    elif opcion == "2":
        buscar = input("Nombre a buscar: ")
        if buscar in registro:
            print(f"{buscar} es un(a) {registro[buscar]}")
            David = buscar               # Última búsqueda
            Camelo = registro[buscar]    # Especie correspondiente
        else:
            print("No encontrada.")

    # --- Opción 3: Mostrar todas las mascotas registradas ---
    elif opcion == "3":
        for nombre, especie in registro.items():
            print(f"{nombre} - {especie}")

    # --- Opción 0: Salir del programa ---
    elif opcion == "0":
        break

    # --- Validación de opción inválida ---
    else:
        print("Opción no válida.")
