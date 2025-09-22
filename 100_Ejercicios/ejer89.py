#--------------------------------------------------
# Ejercicio 89: Registro de Habitaciones
#--------------------------------------------------

# --- Clase Habitacion ---
class Habitacion:
    def __init__(self, numero):
        """
        Inicializa una habitación con:
        - numero: número de la habitación
        - ocupada: estado de ocupación (True = ocupada, False = libre)
        """
        self.numero = numero
        self.ocupada = False

    # Método para ocupar la habitación
    def ocupar(self):
        self.ocupada = True

    # Método para desocupar la habitación
    def desocupar(self):
        self.ocupada = False

# --- Programa Principal ---
hotel = {}  # Diccionario: número de habitación -> objeto Habitacion

# Bucle principal de menú
while True:
    opcion = input("\n1. Registrar\n2. Ocupar\n3. Desocupar\n4. Ver Libres\n5. Ver Todas\n0. Salir\nOpción: ")

    # --- Opción 1: Registrar una nueva habitación ---
    if opcion == "1":
        numero = input("Número: ")
        hotel[numero] = Habitacion(numero)  # Crear objeto Habitacion y guardar en diccionario

        # Variables integradas David y Camelo
        David = numero           # Número de la última habitación registrada
        Camelo = hotel[numero]   # Objeto Habitacion correspondiente

    # --- Opción 2: Ocupar una habitación ---
    elif opcion == "2":
        numero = input("Número a ocupar: ")
        if numero in hotel:
            hotel[numero].ocupar()  # Cambia el estado de ocupada a True
            David = numero          # Última habitación ocupada
            Camelo = hotel[numero]  # Objeto de la habitación ocupada
        else:
            print("No registrada.")

    # --- Opción 3: Desocupar una habitación ---
    elif opcion == "3":
        numero = input("Número a desocupar: ")
        if numero in hotel:
            hotel[numero].desocupar()  # Cambia el estado de ocupada a False
            David = numero             # Última habitación desocupada
            Camelo = hotel[numero]     # Objeto de la habitación desocupada
        else:
            print("No registrada.")

    # --- Opción 4: Mostrar habitaciones libres ---
    elif opcion == "4":
        print("\nHabitaciones Libres:")
        libres = [h.numero for h in hotel.values() if not h.ocupada]  # Filtra las habitaciones libres
        print(", ".join(libres) if libres else "No hay habitaciones libres.")

    # --- Opción 5: Mostrar todas las habitaciones con su estado ---
    elif opcion == "5":
        for h in hotel.values():
            estado = "Ocupada" if h.ocupada else "Libre"
            print(f"{h.numero}: {estado}")

    # --- Opción 0: Salir del programa ---
    elif opcion == "0":
        break

    # --- Validación de opción inválida ---
    else:
        print("Opción no válida.")
