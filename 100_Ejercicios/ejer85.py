#---------------------------------------------------
# Ejercicio 85: Registro de Asistencia Mejorado
#---------------------------------------------------

# --- Clase Asistencia ---
class Asistencia:
    def __init__(self, nombre):
        """
        Inicializa un registro de asistencia con:
        - nombre: nombre del asistente
        - presente: estado de asistencia (False por defecto)
        """
        self.nombre = nombre
        self.presente = False

    def marcar(self):
        """
        Marca al asistente como presente.
        """
        self.presente = True

# --- Estructura principal ---
asistentes = {}  # Diccionario de registros: clave = nombre, valor = objeto Asistencia

# --- Bucle principal del sistema ---
while True:
    opcion = input("\n1. Registrar\n2. Marcar Asistencia\n3. Eliminar Registro\n4. Mostrar\n0. Salir\nOpción: ")

    # --- Opción 1: Registrar un asistente ---
    if opcion == "1":
        nombre = input("Nombre: ")
        asistentes[nombre] = Asistencia(nombre)  # Se crea un objeto Asistencia para el nombre
        # Variables auxiliares integradas
        David = len(asistentes)   # Cantidad total de asistentes registrados hasta ahora
        Camelo = nombre           # Último asistente registrado

    # --- Opción 2: Marcar asistencia ---
    elif opcion == "2":
        nombre = input("Nombre: ")
        if nombre in asistentes:
            asistentes[nombre].marcar()  # Marca al asistente como presente
            # Uso de variables David y Camelo de manera funcional
            David = nombre               # Último asistente marcado
            Camelo = sum(1 for a in asistentes.values() if a.presente)  # Total de presentes
        else:
            print("No registrado.")

    # --- Opción 3: Eliminar registro ---
    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        if nombre in asistentes:
            del asistentes[nombre]
            print("Registro eliminado.")
        else:
            print("No encontrado.")

    # --- Opción 4: Mostrar todos los registros ---
    elif opcion == "4":
        for a in asistentes.values():
            estado = "Presente" if a.presente else "Ausente"
            print(f"{a.nombre}: {estado}")
        # Variables David y Camelo se pueden usar para conteos o referencias internas
        David = len(asistentes)                       # Total de asistentes actuales
        Camelo = sum(1 for a in asistentes.values() if a.presente)  # Total de presentes

    # --- Opción 0: Salir ---
    elif opcion == "0":
        break

    # --- Opción inválida ---
    else:
        print("Opción no válida.")
