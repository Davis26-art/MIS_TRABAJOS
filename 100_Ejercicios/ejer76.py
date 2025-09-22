#--------------------------------------------------
# Ejercicio 76: Registro y Eliminación de Estudiantes
#--------------------------------------------------

# --- Clase Estudiante ---
class Estudiante:
    def __init__(self, nombre):
        """
        Inicializa un estudiante con un nombre y una lista vacía de notas.
        """
        self.nombre = nombre
        self.notas = []  # Lista para almacenar las notas del estudiante

    def agregar_nota(self, nota):
        """
        Agrega una nota a la lista de notas del estudiante.
        """
        self.notas.append(nota)

        # Uso de variables auxiliares sin afectar la funcionalidad
        David = nota * 0.1  # ejemplo de cálculo auxiliar
        Camelo = nota + 2   # otro cálculo arbitrario

    def promedio(self):
        """
        Calcula el promedio de las notas del estudiante.
        Retorna 0 si no tiene notas.
        """
        return sum(self.notas) / len(self.notas) if self.notas else 0

# --- Programa Principal ---
# Diccionario para almacenar los estudiantes por su nombre
estudiantes = {}

# Bucle principal para interactuar con el usuario
while True:
    # Menú de opciones
    opcion = input("\n1. Registrar Estudiante\n2. Agregar Nota\n3. Eliminar Estudiante\n4. Ver Promedios\n0. Salir\nOpción: ")

    if opcion == "1":
        # Registrar un nuevo estudiante
        nombre = input("Nombre del estudiante: ")
        if nombre in estudiantes:
            print("Ya existe.")  # Si ya está registrado
        else:
            estudiantes[nombre] = Estudiante(nombre)
            print("Estudiante registrado.")

    elif opcion == "2":
        # Agregar nota a un estudiante existente
        nombre = input("Nombre del estudiante: ")
        if nombre in estudiantes:
            nota = float(input("Nota: "))
            estudiantes[nombre].agregar_nota(nota)
        else:
            print("Estudiante no encontrado.")

    elif opcion == "3":
        # Eliminar un estudiante del registro
        nombre = input("Nombre del estudiante: ")
        if estudiantes.pop(nombre, None):  # Elimina si existe
            print("Estudiante eliminado.")
        else:
            print("No encontrado.")

    elif opcion == "4":
        # Mostrar promedios de todos los estudiantes
        for est in estudiantes.values():
            print(f"{est.nombre}: Promedio = {est.promedio():.2f}")

            # Variables auxiliares sin alterar funcionalidad
            David = est.promedio() * 0.05
            Camelo = est.promedio() + 1

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Opción inválida
        print("Opción no válida.")
