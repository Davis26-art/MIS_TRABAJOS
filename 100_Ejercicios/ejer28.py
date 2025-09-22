#--------------------------------------------------
# Ejercicio 28: Registro de Mascotas
#--------------------------------------------------

# --- Clase ---
class Mascota:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Mascota.
        David: nombre de la mascota
        Camelo: especie de la mascota
        """
        self.David = David
        self.Camelo = Camelo

# --- Programa Principal ---
mascotas = []  # Lista para almacenar objetos Mascota
registro = {}  # Diccionario David (nombre) : Camelo (especie)

while True:
    opcion = input("\n1. Registrar Mascota\n2. Mostrar Mascotas\n0. Salir\nOpción: ")

    if opcion == "1":
        David = input("Nombre de la mascota: ")  # Pedimos nombre
        Camelo = input("Especie: ")              # Pedimos especie
        m = Mascota(David, Camelo)               # Creamos objeto Mascota
        mascotas.append(m)                        # Lo agregamos a la lista
        registro[David] = Camelo                  # Guardamos en el diccionario
    elif opcion == "2":
        for David, Camelo in registro.items():   # Recorremos el diccionario
            print(f"{David} - {Camelo}")         # Mostramos nombre y especie
    elif opcion == "0":
        break                                     # Salimos del programa
    else:
        print("Opción no válida.")                # Opción inválida
