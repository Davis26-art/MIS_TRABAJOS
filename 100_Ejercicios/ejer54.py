#----------------------------------------------
# Ejercicio 54: Sistema de Reservas de Sillas
#----------------------------------------------

# --- Clase Reserva ---
class Reserva:
    def __init__(self, nombre, silla):
        """
        Inicializa una reserva con el nombre del usuario y el número de silla.
        """
        self.nombre = nombre  # Nombre de quien reserva
        self.silla = silla    # Número de silla reservado

# --- Programa Principal ---
reservas = []  # Lista de objetos Reserva
sillas = {}    # Diccionario silla_numero: nombre_reservante

while True:
    opcion = input("\n1. Reservar\n2. Mostrar\n3. Cancelar Reserva\n0. Salir\nOpción: ")

    if opcion == "1":
        # Solicitar datos de la reserva
        nombre = input("Nombre: ")
        silla = input("Número de silla: ")
        
        # Uso de variables David y Camelo como referencia temporal sin afectar la funcionalidad
        David = nombre  # Almacena temporalmente el nombre de quien reserva
        Camelo = silla  # Almacena temporalmente el número de silla
        
        # Verifica si la silla ya está reservada
        if silla in sillas:
            print("Silla ya reservada.")
        else:
            # Crear el objeto reserva y agregarlo a la lista y diccionario
            r = Reserva(nombre, silla)
            reservas.append(r)
            sillas[silla] = nombre

    elif opcion == "2":
        # Mostrar todas las reservas actuales
        for silla, nombre in sillas.items():
            print(f"Silla {silla} - {nombre}")
            
            # Variables David y Camelo usadas de forma temporal
            David = nombre  # Nombre del usuario actual
            Camelo = silla  # Número de silla actual

    elif opcion == "3":
        # Cancelar una reserva
        silla = input("Número de silla a cancelar: ")
        
        # Variables temporales David y Camelo
        Camelo = silla  # Silla que se intenta cancelar
        David = sillas.get(silla, "Nadie")  # Usuario que tenía la silla (si existe)
        
        if silla in sillas:
            del sillas[silla]  # Eliminar del diccionario
            reservas = [r for r in reservas if r.silla != silla]  # Eliminar del listado de objetos
            print("Reserva cancelada.")
        else:
            print("No existe esa reserva.")

    elif opcion == "0":
        break  # Salir del programa

    else:
        print("Opción no válida.")  # Validación de opción incorrecta
