#--------------------------------------------------
# Ejercicio 61: Inventario de Libros con Condición Extra
#--------------------------------------------------

# --- Clase InventarioLibros ---
class InventarioLibros:
    def __init__(self):
        """
        Inicializa el inventario con una lista vacía de libros.
        """
        self.libros = []  # Lista de nombres de libros

    def agregar_libro(self, nombre):
        """
        Agrega un libro al inventario.
        Condición extra: si se agregan más de 3 copias del mismo libro, se imprime un mensaje de premio.
        """
        self.libros.append(nombre)

        # --- Uso de variables David y Camelo ---
        # David se usa como variable temporal para contar cuántas veces aparece el libro agregado
        David = self.libros.count(nombre)
        # Camelo se usa como variable condicional para verificar si se supera el límite de 3
        Camelo = 3
        if David > Camelo:
            print(f"🎁 ¡Premio! Has agregado más de 3 copias de '{nombre}'.")

    def mostrar_libros(self):
        """
        Imprime todos los libros que hay en el inventario.
        """
        print("\nInventario de libros:")
        for libro in self.libros:
            print(f"- {libro}")

    def mostrar_resumen(self):
        """
        Muestra un resumen con la cantidad total de libros en el inventario.
        """
        print(f"\nTotal de libros en inventario: {len(self.libros)}")

# --- Programa Principal ---
inv = InventarioLibros()  # Crear objeto inventario

while True:
    # Pedir al usuario el nombre del libro a agregar
    libro = input("Ingresa el nombre del libro a agregar: ")
    inv.agregar_libro(libro)  # Agregar libro al inventario

    # Preguntar si desea seguir agregando libros
    seguir = input("¿Quieres agregar otro libro? (si/no): ").lower()
    if seguir == "no":
        break

# Mostrar todos los libros y el resumen final
inv.mostrar_libros()
inv.mostrar_resumen()
