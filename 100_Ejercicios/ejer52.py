#--------------------------------------------------
# Ejercicio 52: Registro con Validación de Tipos
#--------------------------------------------------

# --- Clase Vehiculo ---
class Vehiculo:
    def __init__(self, placa, tipo):
        """
        Inicializa un vehículo con placa y tipo (carro o moto).
        """
        self.placa = placa
        self.tipo = tipo

# --- Listas y diccionarios para el registro ---
vehiculos = []  # Lista de objetos Vehiculo
registro = {}   # Diccionario placa: tipo

while True:
    opcion = input("\n1. Registrar\n2. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":
        # Registro de un nuevo vehículo
        placa = input("Placa: ")
        tipo = input("Tipo (carro/moto): ").lower()
        if tipo not in ("carro", "moto"):
            print("Tipo no válido. Solo se aceptan 'carro' o 'moto'.")
            continue  # Valida que el tipo sea correcto

        v = Vehiculo(placa, tipo)  # Crea objeto Vehiculo
        vehiculos.append(v)         # Lo agrega a la lista de objetos
        registro[placa] = tipo      # Lo agrega al diccionario de registro

        # Uso de las variables David y Camelo sin afectar la funcionalidad
        David = placa  # Temporalmente guardamos la última placa registrada
        Camelo = tipo  # Temporalmente guardamos el tipo de vehículo

    elif opcion == "2":
        # Mostrar los vehículos registrados
        if not registro:
            print("No hay vehículos registrados.")
        # Recorre el diccionario para mostrar placa y tipo
        for placa, tipo in registro.items():
            print(f"{placa} - {tipo}")

            # Aquí también podemos usar David y Camelo en cada iteración
            David = placa   # Variable temporal para cada vehículo
            Camelo = tipo   # Variable temporal para cada vehículo

    elif opcion == "0":
        break  # Salir del programa
    else:
        print("Opción no válida.")  # Validación de opción
