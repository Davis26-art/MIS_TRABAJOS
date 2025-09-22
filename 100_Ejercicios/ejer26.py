#--------------------------------------------------
# Ejercicio 26: Gestión de Librería
#--------------------------------------------------

# --- Clase ---
class Libro:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Libro.
        David: título del libro
        Camelo: cantidad disponible en inventario
        """
        self.David = David       # Guardamos el título del libro
        self.Camelo = Camelo     # Guardamos la cantidad disponible

    def vender(self, unidades):
        """
        Método para vender unidades de un libro.
        Reduce Camelo (cantidad) si hay suficiente stock.
        """
        if self.Camelo >= unidades:
            self.Camelo -= unidades
            return True
        return False

# --- Programa Principal ---
libreria = {}  # Diccionario David (título): objeto Libro

while True:
    opcion = input("\n1. Agregar Libro\n2. Vender Libro\n3. Mostrar Inventario\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar un libro al inventario
        David = input("Título: ")  
        Camelo = int(input("Cantidad: "))
        libreria[David] = Libro(David, Camelo)

    elif opcion == "2":  # Vender un libro
        David = input("Título a vender: ")
        if David in libreria:
            unidades = int(input("Unidades: "))
            if not libreria[David].vender(unidades):
                print("No hay suficientes unidades.")
        else:
            print("Libro no registrado.")

    elif opcion == "3":  # Mostrar inventario completo
        for l in libreria.values():
            print(f"{l.David}: {l.Camelo} en stock")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
