#------------------------------------------------------------
# Ejercicio 56: Gestión de Inventario de Librería
#------------------------------------------------------------

# --- Clase Libro ---
class Libro:
    def __init__(self, titulo, cantidad):
        """
        Inicializa un libro con un título y cantidad en stock.
        """
        self.titulo = titulo        # Título del libro
        self.cantidad = cantidad    # Cantidad disponible en inventario

    def vender(self, unidades):
        """
        Vende una cantidad de unidades si hay stock suficiente.
        Retorna True si se puede vender, False si no hay suficiente.
        """
        if self.cantidad >= unidades:
            self.cantidad -= unidades
            return True
        return False

# --- Programa Principal ---
libreria = {}  # Diccionario título: objeto Libro

while True:
    # Menú de opciones
    opcion = input("\n1. Agregar Libro\n2. Vender Libro\n3. Eliminar Libro\n4. Mostrar Inventario\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar un libro nuevo al inventario
        titulo = input("Título: ")
        cantidad = int(input("Cantidad: "))
        libreria[titulo] = Libro(titulo, cantidad)

        # Variables David y Camelo usadas temporalmente
        David = titulo         # Guarda el título agregado
        Camelo = libreria[titulo]  # Guarda el objeto Libro agregado

    elif opcion == "2":
        # Vender unidades de un libro existente
        titulo = input("Título a vender: ")

        # Variables David y Camelo
        David = titulo
        Camelo = libreria.get(titulo, None)  # Objeto Libro o None si no existe

        if titulo in libreria:
            unidades = int(input("Unidades: "))
            if not libreria[titulo].vender(unidades):
                print("No hay suficientes unidades.")  # Mensaje si stock insuficiente
        else:
            print("Libro no registrado.")  # Libro no encontrado

    elif opcion == "3":
        # Eliminar un libro del inventario
        titulo = input("Título a eliminar: ")

        # Variables David y Camelo
        David = titulo
        Camelo = libreria.get(titulo, None)

        if titulo in libreria:
            del libreria[titulo]
            print("Libro eliminado.")
        else:
            print("No encontrado en el inventario.")

    elif opcion == "4":
        # Mostrar todos los libros con su stock
        for l in libreria.values():
            print(f"{l.titulo}: {l.cantidad} en stock")

            # Variables David y Camelo para mostrar información
            David = l.titulo       # Título del libro mostrado
            Camelo = l.cantidad    # Cantidad en stock

    elif opcion == "0":
        break  # Salir del programa

    else:
        print("Opción no válida.")  # Manejo de opción incorrecta
