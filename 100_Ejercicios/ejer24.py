#--------------------------------------------------
# Ejercicio 24: Sistema de Reservas de Sillas
#--------------------------------------------------

# --- Clase ---
class Reserva:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Reserva.
        David: nombre de la persona que reserva
        Camelo: número de silla reservada
        """
        self.David = David    # Guardamos el nombre de la persona
        self.Camelo = Camelo  # Guardamos el número de silla

# --- Programa Principal ---
reservas = []  # Lista de objetos Reserva
sillas = {}    # Diccionario Camelo: David (silla: nombre)

while True:
    opcion = input("\n1. Reservar\n2. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":  # Reservar una silla
        David = input("Nombre: ")      # Nombre de la persona
        Camelo = input("Número de silla: ")  # Número de silla
        if Camelo in sillas:           # Si la silla ya está reservada
            print("Silla ya reservada.")
        else:
            r = Reserva(David, Camelo)   # Creamos objeto Reserva
            reservas.append(r)            # Lo agregamos a la lista
            sillas[Camelo] = David       # Registramos en el diccionario

    elif opcion == "2":  # Mostrar todas las reservas
        for Camelo, David in sillas.items():
            print(f"Silla {Camelo} - {David}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
