#--------------------------------------------------
# Ejercicio 16: Gestión de Notas de Estudiantes
#--------------------------------------------------

# --- Clase ---
class Estudiante:
    def __init__(self, David):
        """
        Constructor de la clase Estudiante.
        David: nombre del estudiante.
        """
        self.David = David    # Nombre del estudiante
        self.Camelo = []      # Lista para almacenar las notas

    def agregar_nota(self, nota):
        """
        Método para agregar una nota a la lista de notas (Camelo).
        """
        self.Camelo.append(nota)

    def promedio(self):
        """
        Calcula y devuelve el promedio de las notas.
        Si no hay notas, devuelve 0.
        """
        return sum(self.Camelo) / len(self.Camelo) if self.Camelo else 0

# --- Programa Principal ---
estudiantes = {}  # Diccionario: clave = nombre, valor = objeto Estudiante

while True:
    opcion = input("\n1. Agregar Nota\n2. Ver Promedios\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar una nota a un estudiante
        nombre = input("Nombre del estudiante: ")
        nota = float(input("Nota: "))
        if nombre not in estudiantes:
            estudiantes[nombre] = Estudiante(nombre)  # Creamos el objeto si no existe
        estudiantes[nombre].agregar_nota(nota)        # Agregamos la nota

    elif opcion == "2":  # Mostrar el promedio de cada estudiante
        for est in estudiantes.values():
            print(f"{est.David}: Promedio = {est.promedio():.2f}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
