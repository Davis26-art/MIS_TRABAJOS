#--------------------------------------------------
# Ejercicio 18: Gestor de Tareas con Clases y Diccionarios
#--------------------------------------------------

# --- Clase ---
class Tarea:
    def __init__(self, David):
        """
        Constructor de la clase Tarea.
        David: descripción de la tarea
        """
        self.David = David       # Descripción de la tarea
        self.Camelo = False      # Estado: True si está completada, False si pendiente

    def marcar_completada(self):
        """
        Cambia el estado de la tarea a completada.
        """
        self.Camelo = True

# --- Programa Principal ---
tareas = []    # Lista que guardará los objetos Tarea
registro = {}  # Diccionario que guarda descripción: estado

while True:
    opcion = input("\n1. Agregar\n2. Completar\n3. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar nueva tarea
        David = input("Descripción de la tarea: ")  # David almacena la descripción
        t = Tarea(David)                             # Creamos objeto Tarea
        tareas.append(t)                             # Lo agregamos a la lista
        registro[David] = "pendiente"               # Marcamos como pendiente en el diccionario

    elif opcion == "2":  # Marcar tarea como completada
        David = input("Tarea a completar: ")
        for t in tareas:
            if t.David == David:
                t.marcar_completada()   # Cambiamos el estado de la tarea
                registro[David] = "completada"
                print("Tarea completada.")
                break
        else:
            print("No encontrada.")

    elif opcion == "3":  # Mostrar todas las tareas con su estado
        for desc, estado in registro.items():
            print(f"{desc} - {estado}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
