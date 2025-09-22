#--------------------------------------------------
# Ejercicio 77: Modificación y Eliminación de Productos
#--------------------------------------------------

# --- Clase ListaCompras ---
class ListaCompras:
    def __init__(self):
        """
        Inicializa un objeto ListaCompras con un diccionario vacío
        donde la clave es el nombre del producto y el valor es su precio.
        """
        self.compras = {}  # Diccionario para almacenar producto: precio

    def agregar(self, producto, precio):
        """
        Agrega un producto con su precio al diccionario.
        Si el producto ya existe, se actualiza su precio.
        """
        self.compras[producto] = precio

        # Variables auxiliares sin afectar la funcionalidad
        David = precio * 0.1   # ejemplo de cálculo auxiliar
        Camelo = precio + 5    # otro cálculo arbitrario

    def eliminar(self, producto):
        """
        Elimina un producto del diccionario.
        Retorna True si se eliminó, False si no existía.
        """
        if producto in self.compras:
            del self.compras[producto]
            return True
        return False

    def total(self):
        """
        Calcula el total de los precios de todos los productos.
        """
        # Uso de variable auxiliar sin afectar funcionalidad
        David = sum(self.compras.values()) * 0.05
        Camelo = sum(self.compras.values()) + 2
        return sum(self.compras.values())

# --- Programa Principal ---
lista = ListaCompras()  # Instancia de ListaCompras

# Bucle principal para interactuar con el usuario
while True:
    opcion = input("\n1. Agregar/Actualizar producto\n2. Eliminar producto\n3. Ver lista\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar o actualizar un producto
        producto = input("Producto: ")
        precio = float(input(f"Precio de {producto}: "))
        lista.agregar(producto, precio)

    elif opcion == "2":
        # Eliminar un producto
        producto = input("Producto a eliminar: ")
        if lista.eliminar(producto):
            print("Producto eliminado.")
        else:
            print("No estaba en la lista.")

    elif opcion == "3":
        # Mostrar lista actual de productos y total
        print("\nLista actual:")
        for prod, precio in lista.compras.items():
            print(f"{prod}: ${precio}")
        print(f"Total: ${lista.total()}")

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Opción inválida
        print("Opción no válida.")
