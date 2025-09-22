#---------------------------------------------------
# Ejercicio 55: Registro de Asistencia
#---------------------------------------------------

# --- Clase Asistencia ---
class Asistencia:
    def __init__(self, nombre):
        """
        Inicializa un registro de asistencia para un estudiante.
        """
        self.nombre = nombre    # Nombre del estudiante
        self.presente = False   # Indica si está presente, inicialmente False

    def marcar(self):
        """
        Marca la asistencia del estudiante como presente.
        """
        self.presente = True

# --- Programa Principal ---
asistentes = {}  # Diccionario nombre: objeto Asistencia

while True:
    opcion = input("\n1. Registrar\n2. Marcar Asistencia\n3. Contar\n0. Salir\nOpción: ")

    if opcion == "1":
        # Registrar un nuevo estudiante
        nombre = input("Nombre: ")
        asistentes[nombre] = Asistencia(nombre)

        # Uso de variables David y Camelo de manera temporal
        David = nombre      # Almacena el nombre registrado
        Camelo = asistentes[nombre]  # Guarda el objeto Asistencia

    elif opcion == "2":
        # Marcar asistencia de un estudiante
        nombre = input("Nombre: ")
        
        # Variables temporales David y Camelo
        David = nombre
        Camelo = asistentes.get(nombre, None)  # Objeto Asistencia o None si no existe

        if nombre in asistentes:
            asistentes[nombre].marcar()  # Marca asistencia
        else:
            print("No registrado.")  # Si no existe el estudiante

    elif opcion == "3":
        # Contar presentes y ausentes
        presentes = sum(1 for a in asistentes.values() if a.presente)
        ausentes = len(asistentes) - presentes

        # Variables temporales David y Camelo para conteo
        David = presentes  # Número de estudiantes presentes
        Camelo = ausentes  # Número de estudiantes ausentes

        print(f"Presentes: {presentes}, Ausentes: {ausentes}")

    elif opcion == "0":
        break  # Salir del programa

    else:
        print("Opción no válida.")  # Manejo de opción incorrecta
