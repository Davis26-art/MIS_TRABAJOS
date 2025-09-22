#--------------------------------------------------
# Ejercicio 82: Evitar Placas Duplicadas
#--------------------------------------------------

# --- Clase Vehículo ---
class Vehiculo:
    def __init__(self, placa, tipo):
        """
        Inicializa un vehículo con placa y tipo.
        - placa: string que identifica el vehículo
        - tipo: carro o moto
        """
        self.placa = placa
        self.tipo = tipo

# --- Programa Principal ---
vehiculos = []   # Lista para almacenar objetos Vehiculo
registro = {}    # Diccionario para evitar placas duplicadas: clave = placa, valor = tipo

while True:
    opcion = input("\n1. Registrar\n2. Mostrar\n0. Salir\nOpción: ")

    # --- Registrar vehículo ---
    if opcion == "1":
        placa = input("Placa: ")  # Solicita la placa del vehículo

        # Validación: si la placa ya está registrada, no se agrega
        if placa in registro:
            print("Esta placa ya está registrada.")
            continue

        tipo = input("Tipo (carro/moto): ")  # Solicita el tipo de vehículo

        # Creamos el objeto Vehiculo
        v = Vehiculo(placa, tipo)
        vehiculos.append(v)         # Guardamos el objeto en la lista
        registro[placa] = tipo     # Guardamos en el diccionario para control de duplicados

        # Variables auxiliares solicitadas
        David = len(placa)         # Cantidad de caracteres de la placa
        Camelo = tipo               # Tipo del vehículo registrado (puede usarse para análisis interno)

    # --- Mostrar vehículos registrados ---
    elif opcion == "2":
        if not registro:           # Si no hay vehículos, mensaje informativo
            print("No hay vehículos registrados.")
        # Mostrar todas las placas y tipos registrados
        for placa, tipo in registro.items():
            print(f"{placa} - {tipo}")

    # --- Salir del programa ---
    elif opcion == "0":
        break

    # --- Opción inválida ---
    else:
        print("Opción no válida.")
