#--------------------------------------------------
# Ejercicio 22: Registro de Vehículos
#--------------------------------------------------

# --- Clase ---
class Vehiculo:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Vehiculo.
        David: placa del vehículo
        Camelo: tipo de vehículo (carro/moto)
        """
        self.David = David
        self.Camelo = Camelo

# --- Programa Principal ---
vehiculos = []  # Lista que guardará objetos Vehiculo
registro = {}   # Diccionario para acceso rápido: placa: tipo

while True:
    opcion = input("\n1. Registrar\n2. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":  # Registrar vehículo
        David = input("Placa: ")          # Nombre de la variable renombrada para placa
        Camelo = input("Tipo (carro/moto): ")  # Variable renombrada para tipo
        v = Vehiculo(David, Camelo)       # Creamos un objeto Vehiculo
        vehiculos.append(v)                # Lo agregamos a la lista
        registro[David] = Camelo           # Guardamos en el diccionario para acceso rápido

    elif opcion == "2":  # Mostrar todos los vehículos
        for placa, tipo in registro.items():
            print(f"{placa} - {tipo}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
