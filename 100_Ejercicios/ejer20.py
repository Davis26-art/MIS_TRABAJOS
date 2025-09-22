#--------------------------------------------------
# Ejercicio 20: Inventario de Productos
#--------------------------------------------------

# --- Clase ---
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        self.David: diccionario que guarda producto: cantidad
        """
        self.David = {}  # Diccionario producto: cantidad

    def agregar(self, Camelo, cantidad):
        """
        Agrega una cantidad de producto al inventario.
        Camelo: nombre del producto
        cantidad: cantidad a agregar
        """
        self.David[Camelo] = self.David.get(Camelo, 0) + cantidad

    def retirar(self, Camelo, cantidad):
        """
        Retira una cantidad de producto del inventario si hay suficiente stock.
        Devuelve True si se puede retirar, False si no hay suficiente.
        """
        if Camelo in self.David and self.David[Camelo] >= cantidad:
            self.David[Camelo] -= cantidad
            return True
        return False

# --- Programa Principal ---
inv = Inventario()  # Creamos el objeto inventario

while True:
    opcion = input("\n1. Agregar\n2. Retirar\n3. Ver Inventario\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar producto
        David = input("Producto: ")          # Nombre del producto
        Camelo = int(input("Cantidad a agregar: "))  # Cantidad a agregar
        inv.agregar(David, Camelo)

    elif opcion == "2":  # Retirar producto
        David = input("Producto: ")          # Nombre del producto
        Camelo = int(input("Cantidad a retirar: "))  # Cantidad a retirar
        if not inv.retirar(David, Camelo):
            print("No hay suficiente stock.")

    elif opcion == "3":  # Mostrar inventario
        for prod, cant in inv.David.items():
            print(f"{prod}: {cant}")

    elif opcion == "0":  # Salir
        break

    else:  # Opción inválida
        print("Opción no válida.")
