#--------------------------------------------------
# Ejercicio 25: Registro de Asistencia
#--------------------------------------------------

# --- Clase ---
class Asistencia:
    def __init__(self, David):
        """
        Constructor de la clase Asistencia.
        David: nombre del asistente
        """
        self.David = David       # Guardamos el nombre del asistente
        self.Camelo = False      # Booleano para marcar si está presente (False = ausente)

    def marcar(self):
        """
        Método para marcar asistencia.
        Cambia Camelo a True, indicando que la persona está presente.
        """
        self.Camelo = True

# --- Programa Principal ---
asistentes = {}  # Diccionario David: objeto Asistencia

while True:
    opcion = input("\n1. Registrar\n2. Marcar Asistencia\n3. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":  # Registrar un asistente
        David = input("Nombre: ")             # Nombre del asistente
        asistentes[David] = Asistencia(David) # Creamos y guardamos el objeto Asistencia

    elif opcion == "2":  # Marcar asistencia
        David = input("Nombre: ")  
        if David in asistentes:               # Si la persona está registrada
            asistentes[David].marcar()       # Marcamos asistencia
        else:
            print("No registrado.")          # Aviso si no estaba registrado

    elif opcion == "3":  # Mostrar estado de asistencia
        for a in asistentes.values():
            estado = "Presente" if a.Camelo else "Ausente"  # Usamos Camelo para verificar
            print(f"{a.David}: {estado}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
