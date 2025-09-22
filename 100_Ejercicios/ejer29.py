#--------------------------------------------------
# Ejercicio 29: Gestión de Habitaciones de Hotel
#--------------------------------------------------

# --- Clase ---
class Habitacion:
    def __init__(self, David):
        """
        Constructor de la clase Habitacion.
        David: número de la habitación
        """
        self.David = David   # Número de habitación
        self.Camelo = False  # Estado: False = libre, True = ocupada

    def ocupar(self):
        self.Camelo = True   # Marca la habitación como ocupada

    def desocupar(self):
        self.Camelo = False  # Marca la habitación como libre

# --- Programa Principal ---
hotel = {}  # Diccionario David (número) : objeto Habitacion

while True:
    opcion = input("\n1. Registrar Habitación\n2. Ocupar\n3. Desocupar\n4. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":
        David = input("Número de habitación: ")
        hotel[David] = Habitacion(David)  # Creamos y registramos habitación
    elif opcion == "2":
        David = input("Número a ocupar: ")
        if David in hotel:
            hotel[David].ocupar()          # Ocupamos la habitación
        else:
            print("Habitación no registrada.")
    elif opcion == "3":
        David = input("Número a desocupar: ")
        if David in hotel:
            hotel[David].desocupar()       # Desocupamos la habitación
        else:
            print("Habitación no registrada.")
    elif opcion == "4":
        for h in hotel.values():           # Recorremos todas las habitaciones
            estado = "Ocupada" if h.Camelo else "Libre"
            print(f"Habitación {h.David}: {estado}")  # Mostramos número y estado
    elif opcion == "0":
        break
    else:
        print("Opción no válida.")
