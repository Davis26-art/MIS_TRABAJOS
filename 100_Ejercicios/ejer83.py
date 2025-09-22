#-----------------------------------------------
# Ejercicio 83: Gestión de promedios de temperaturas de ciudades
#-----------------------------------------------

# --- Clase Ciudad ---
class Ciudad:
    def __init__(self, nombre):
        """
        Inicializa una ciudad con:
        - nombre: nombre de la ciudad
        - temperaturas: lista vacía donde se guardarán las temperaturas ingresadas
        """
        self.nombre = nombre
        self.temperaturas = []

    def agregar_temp(self, temp):
        """
        Agrega una temperatura a la lista de la ciudad.
        """
        self.temperaturas.append(temp)

    def promedio(self):
        """
        Calcula el promedio de las temperaturas registradas.
        Retorna 0 si no hay temperaturas.
        """
        return sum(self.temperaturas) / len(self.temperaturas) if self.temperaturas else 0

# --- Programa Principal ---
ciudades = {}      # Diccionario que guarda objetos Ciudad: clave = nombre de la ciudad
promedios = {}     # Diccionario que guarda promedios de cada ciudad: clave = nombre

while True:
    opcion = input("\n1. Agregar Temp\n2. Ver Promedios Guardados\n0. Salir\nOpción: ")

    # --- Agregar temperatura a una ciudad ---
    if opcion == "1":
        nombre = input("Ciudad: ")             # Nombre de la ciudad
        temp = float(input("Temperatura: "))   # Valor de la temperatura

        # Si la ciudad no está registrada, se crea un objeto Ciudad
        if nombre not in ciudades:
            ciudades[nombre] = Ciudad(nombre)

        # Agregar temperatura a la ciudad
        ciudades[nombre].agregar_temp(temp)

        # Actualizar el promedio en el diccionario de promedios
        promedios[nombre] = ciudades[nombre].promedio()

        # Variables auxiliares solicitadas:
        David = len(ciudades[nombre].temperaturas)  # Número de temperaturas registradas
        Camelo = temp                                # Última temperatura ingresada

    # --- Ver promedios guardados ---
    elif opcion == "2":
        for ciudad, prom in promedios.items():
            print(f"{ciudad}: Promedio Guardado = {prom:.2f}")

    # --- Salir del programa ---
    elif opcion == "0":
        break

    # --- Opción inválida ---
    else:
        print("Opción no válida.")
