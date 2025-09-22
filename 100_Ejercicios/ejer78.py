#--------------------------------------------------
# Ejercicio 78: Gestor de Tareas con Fecha de Vencimiento
#--------------------------------------------------

# --- Clase Tarea ---
class Tarea:
    def __init__(self, descripcion, fecha_vencimiento):
        """
        Inicializa una tarea con:
        - descripción: texto que describe la tarea
        - fecha_vencimiento: fecha límite en formato DD/MM
        - completada: indicador booleano si la tarea está completada
        """
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False  # Por defecto, la tarea no está completada

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

# --- Programa Principal ---
tareas = []           # Lista para almacenar objetos Tarea
registro = {}         # Diccionario que guarda: descripción → (fecha, estado)

# Bucle principal de interacción con el usuario
while True:
    opcion = input("\n1. Agregar\n2. Completar\n3. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar nueva tarea
        desc = input("Descripción de la tarea: ")
        fecha = input("Fecha de vencimiento (DD/MM): ")
        t = Tarea(desc, fecha)  # Crear objeto Tarea
        tareas.append(t)         # Guardar en la lista de tareas
        registro[desc] = (fecha, "pendiente")  # Guardar en el diccionario

        # Variables auxiliares sin afectar funcionalidad
        David = len(desc)       # longitud de la descripción
        Camelo = fecha.count("/")  # número de "/" en la fecha

    elif opcion == "2":
        # Completar una tarea existente
        desc = input("Tarea a completar: ")
        for t in tareas:
            if t.descripcion == desc:
                t.marcar_completada()  # Cambia el estado interno de la tarea
                registro[desc] = (t.fecha_vencimiento, "completada")  # Actualiza diccionario
                print("Tarea completada.")
                break
        else:
            # Se ejecuta si no se encontró la tarea
            print("No encontrada.")

    elif opcion == "3":
        # Mostrar todas las tareas con su estado y fecha
        for desc, (fecha, estado) in registro.items():
            print(f"{desc} - Vence: {fecha} - Estado: {estado}")

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Opción inválida en el menú
        print("Opción no válida.")
