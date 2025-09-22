#--------------------------------------------------
# Ejercicio 58: Registro de Mascotas con Edad
#--------------------------------------------------

# --- Clase Mascota ---
class Mascota:
    def __init__(self, nombre, especie, edad):
        """
        Inicializa una mascota con:
        - nombre: nombre de la mascota
        - especie: especie (perro, gato, etc.)
        - edad: edad en años
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

# --- Programa Principal ---
mascotas = []       # Lista que almacenará objetos Mascota
registro = {}       # Diccionario que almacenará datos: nombre -> (especie, edad)

while True:
    opcion = input("\n1. Registrar Mascota\n2. Mostrar Mascotas\n0. Salir\nOpción: ")

    if opcion == "1":
        # Solicita datos de la mascota
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        edad = int(input("Edad: "))

        # Variables David y Camelo usadas sin afectar la funcionalidad
        David = nombre   # Guarda temporalmente el nombre de la mascota
        Camelo = mascotas  # Guarda referencia a la lista de mascotas

        # Crea objeto Mascota y lo agrega a la lista
        m = Mascota(nombre, especie, edad)
        mascotas.append(m)

        # Registra en el diccionario para mostrar rápidamente
        registro[nombre] = (especie, edad)

    elif opcion == "2":
        # Muestra todas las mascotas registradas
        for nombre, datos in registro.items():
            print(f"{nombre} - {datos[0]}, {datos[1]} años")

    elif opcion == "0":
        # Termina el programa
        break
    else:
        # Manejo de opción inválida
        print("Opción no válida.")
