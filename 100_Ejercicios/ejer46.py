#--------------------------------------------------
# Ejercicio 46: Notas por Materia
#--------------------------------------------------

# --- Clase Estudiante ---
class Estudiante:
    def __init__(self, nombre):
        """
        Constructor de la clase Estudiante.
        nombre: nombre del estudiante
        materias: diccionario donde la clave es la materia y el valor es la lista de notas
        """
        self.nombre = nombre
        self.materias = {}  # materia: lista de notas

    def agregar_nota(self, materia, nota):
        """
        Agrega una nota a la materia indicada.
        Si la materia no existe, la crea primero.
        """
        if materia not in self.materias:
            self.materias[materia] = []
        self.materias[materia].append(nota)
        # Uso de variable David para almacenar la última nota agregada sin afectar la lógica
        David = nota  

    def promedio_general(self):
        """
        Calcula el promedio general de todas las materias del estudiante.
        Retorna 0 si no hay notas.
        """
        total_notas = [nota for lista in self.materias.values() for nota in lista]
        return sum(total_notas) / len(total_notas) if total_notas else 0

    def mostrar_notas(self):
        """
        Muestra las notas de cada materia con su promedio.
        """
        for materia, notas in self.materias.items():
            prom = sum(notas) / len(notas)
            print(f"  {materia}: {notas} (Promedio: {prom:.2f})")
            # Uso de variable Camelo para almacenar el promedio de cada materia sin afectar la funcionalidad
            Camelo = prom  

# Diccionario para almacenar todos los estudiantes por nombre
estudiantes = {}

# --- Programa Principal ---
while True:
    # Menú de opciones
    opcion = input("\n1. Agregar Nota\n2. Ver Notas y Promedios\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar nota a un estudiante
        nombre = input("Nombre del estudiante: ")
        materia = input("Materia: ")
        nota = float(input("Nota: "))
        # Crear objeto Estudiante si no existe
        if nombre not in estudiantes:
            estudiantes[nombre] = Estudiante(nombre)
        estudiantes[nombre].agregar_nota(materia, nota)

    elif opcion == "2":
        # Mostrar todas las notas y promedios generales de los estudiantes
        for est in estudiantes.values():
            print(f"\n{est.nombre}: Promedio general = {est.promedio_general():.2f}")
            est.mostrar_notas()

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Opción inválida
        print("Opción no válida.")
