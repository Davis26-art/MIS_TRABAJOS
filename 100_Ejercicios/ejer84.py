#----------------------------------------------
# Ejercicio 84: Sistema de Reservas de Sillas con Disponibilidad
#----------------------------------------------

# --- Clase Reserva ---
class Reserva:
    def __init__(self, nombre, silla):
        """
        Inicializa una reserva con:
        - nombre: nombre de la persona que reserva
        - silla: número de silla reservada
        """
        self.nombre = nombre
        self.silla = silla

# --- Estructuras de datos principales ---
reservas = []      # Lista que almacena objetos Reserva
sillas = {}        # Diccionario que guarda las sillas ocupadas: clave = número de silla, valor = nombre
TOTAL_SILLAS = 10  # Número total de sillas disponibles

# --- Bucle principal del sistema ---
while True:
    opcion = input("\n1. Reservar\n2. Mostrar\n3. Ver Libres\n0. Salir\nOpción: ")

    # --- Opción 1: Reservar una silla ---
    if opcion == "1":
        nombre = input("Nombre: ")        # Nombre del usuario
        silla = input("Número de silla: ")  # Número de silla deseado

        # Comprobación de disponibilidad
        if silla in sillas:
            print("Silla ya reservada.")
        else:
            r = Reserva(nombre, silla)  # Se crea el objeto reserva
            reservas.append(r)           # Se agrega a la lista de reservas
            sillas[silla] = nombre       # Se marca la silla como ocupada en el diccionario

            # Variables auxiliares integradas
            David = len(reservas)        # Cantidad total de reservas realizadas
            Camelo = silla               # Última silla reservada

    # --- Opción 2: Mostrar todas las reservas ---
    elif opcion == "2":
        for silla, nombre in sillas.items():
            print(f"Silla {silla} - {nombre}")

    # --- Opción 3: Mostrar sillas libres ---
    elif opcion == "3":
        print("Sillas libres:")
        for i in range(1, TOTAL_SILLAS + 1):
            if str(i) not in sillas:
                print(f"Silla {i}")

    # --- Opción 0: Salir del programa ---
    elif opcion == "0":
        break

    # --- Opción inválida ---
    else:
        print("Opción no válida.")
