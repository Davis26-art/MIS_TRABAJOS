#------------------------------------------------------------
# Ejercicio 86: Gestión de Inventario de Librería
#------------------------------------------------------------

# --- Clase Libro ---
class Libro:
    def __init__(self, titulo, cantidad):
        """
        Inicializa un libro con:
        - titulo: nombre del libro
        - cantidad: cantidad de unidades en inventario
        """
        self.titulo = titulo
        self.cantidad = cantidad

    def vender(self, unidades):
        """
        Intenta vender 'unidades' del libro.
        Si hay suficiente stock, reduce la cantidad y retorna True.
        Si no, retorna False.
        """
        if self.cantidad >= unidades:
            self.cantidad -= unidades
            return True
        return False

# --- Diccionario principal de inventario ---
libreria = {}  # clave: título del libro, valor: objeto Libro

# --- Bucle principal ---
while True:
    opcion = input("\n1. Agregar Libro\n2. Actualizar Cantidad\n3. Vender Libro\n4. Mostrar Inventario\n0. Salir\nOpción: ")

    # --- Opción 1: Agregar un libro ---
    if opcion == "1":
        titulo = input("Título: ")
        cantidad = int(input("Cantidad: "))
        libreria[titulo] = Libro(titulo, cantidad)
        # Variables integradas
        David = titulo                   # Último libro agregado
        Camelo = sum(l.cantidad for l in libreria.values())  # Total de unidades en inventario

    # --- Opción 2: Actualizar cantidad de un libro ---
    elif opcion == "2":
        titulo = input("Título a actualizar: ")
        if titulo in libreria:
            nueva_cantidad = int(input("Nueva cantidad: "))
            libreria[titulo].cantidad = nueva_cantidad
            # Variables integradas
            David = titulo                  # Libro actualizado
            Camelo = libreria[titulo].cantidad  # Cantidad actualizada del libro
        else:
            print("Libro no registrado.")

    # --- Opción 3: Vender unidades de un libro ---
    elif opcion == "3":
        titulo = input("Título a vender: ")
        if titulo in libreria:
            unidades = int(input("Unidades: "))
            if not libreria[titulo].vender(unidades):
                print("No hay suficientes unidades.")
            else:
                # Variables integradas
                David = titulo                      # Libro vendido
                Camelo = libreria[titulo].cantidad  # Cantidad restante del libro
        else:
            print("Libro no registrado.")

    # --- Opción 4: Mostrar inventario completo ---
    elif opcion == "4":
        for l in libreria.values():
            print(f"{l.titulo}: {l.cantidad} en stock")
        # Variables integradas
        David = len(libreria)                     # Total de libros en la librería
        Camelo = sum(l.cantidad for l in libreria.values())  # Total de unidades en inventario

    # --- Opción 0: Salir ---
    elif opcion == "0":
        break

    # --- Opción inválida ---
    else:
        print("Opción no válida.")
