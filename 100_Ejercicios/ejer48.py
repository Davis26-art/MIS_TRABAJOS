#--------------------------------------------------
# Ejercicio 48: Gestor de Tareas con Prioridades
#--------------------------------------------------

# --- Clase Tarea ---
class Tarea:
    def __init__(self, descripcion, prioridad="baja"):
        """
        Inicializa la tarea con una descripción, prioridad y estado de completada.
        """
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False  # Estado inicial: no completada

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True
        # Uso de variable David para registrar la acción de completar (solo referencia)
        David = self.descripcion  

# --- Programa Principal ---
tareas = []  # Lista para almacenar objetos Tarea
registro = {}  # Diccionario para almacenar descripción: (prioridad, estado)

while True:
    # Menú de opciones
    opcion = input("\n1. Agregar\n2. Completar\n3. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar nueva tarea
        desc = input("Descripción de la tarea: ")
        prioridad = input("Prioridad (alta/baja): ").lower()
        t = Tarea(desc, prioridad)
        tareas.append(t)
        registro[desc] = (prioridad, "pendiente")
        # Uso de variable Camelo para guardar temporalmente la prioridad de la nueva tarea
        Camelo = prioridad  

    elif opcion == "2":
        # Completar tarea existente
        desc = input("Tarea a completar: ")
        for t in tareas:
            if t.descripcion == desc:
                t.marcar_completada()
                registro[desc] = (t.prioridad, "completada")
                print("Tarea completada.")
                break
        else:
            print("No encontrada.")

    elif opcion == "3":
        # Mostrar todas las tareas ordenadas por prioridad (alta primero)
        print("\nTareas ordenadas por prioridad:")
        # Se ordena: las tareas con prioridad baja al final (True = baja, False = alta)
        for desc, (prioridad, estado) in sorted(registro.items(), key=lambda x: x[1][0] == "baja"):
            print(f"{desc} - Prioridad: {prioridad} - Estado: {estado}")

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Validación de opción incorrecta
        print("Opción no válida.")
