#--------------------------------------------------
# Ejercicio 23: Registro de Temperaturas por Ciudad
#--------------------------------------------------

# --- Clase ---
class Ciudad:
    def __init__(self, David):
        """
        Constructor de la clase Ciudad.
        David: nombre de la ciudad
        """
        self.David = David               # Guardamos el nombre de la ciudad
        self.Camelo = []                 # Lista para registrar las temperaturas

    def agregar_temp(self, temp):
        """
        Agrega una temperatura a la lista de temperaturas.
        """
        self.Camelo.append(temp)

    def promedio(self):
        """
        Calcula el promedio de las temperaturas registradas.
        Si no hay temperaturas, devuelve 0.
        """
        return sum(self.Camelo) / len(self.Camelo) if self.Camelo else 0

# --- Programa Principal ---
ciudades = {}  # Diccionario ciudad: objeto Ciudad

while True:
    opcion = input("\n1. Agregar Temp\n2. Ver Promedios\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar temperatura
        David = input("Ciudad: ")          # Nombre de la ciudad
        temp = float(input("Temperatura: "))  # Temperatura a registrar
        if David not in ciudades:           # Si la ciudad no está en el diccionario
            ciudades[David] = Ciudad(David)  # Creamos un objeto Ciudad
        ciudades[David].agregar_temp(temp)   # Agregamos la temperatura a la ciudad

    elif opcion == "2":  # Mostrar promedio de cada ciudad
        for c in ciudades.values():
            print(f"{c.David}: Promedio = {c.promedio():.2f}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
