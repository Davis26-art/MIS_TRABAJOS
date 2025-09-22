#--------------------------------------------------
# Ejercicio 80: Inventario con Total de Unidades
#--------------------------------------------------

# --- Clase Inventario ---
class Inventario:
    def __init__(self):
        """
        Inicializa un inventario vacío como un diccionario.
        Clave: nombre del producto
        Valor: cantidad disponible
        """
        self.productos = {}

    def agregar(self, producto, cantidad):
        """
        Agrega una cantidad de un producto al inventario.
        Si el producto no existe, se crea; si existe, se suma la cantidad.
        """
        self.productos[producto] = self.productos.get(producto, 0) + cantidad

    def retirar(self, producto, cantidad):
        """
        Retira una cantidad de un producto si hay suficiente stock.
        Retorna True si se pudo retirar, False si no hay suficiente.
        """
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        return False

    def total_unidades(self):
        """
        Retorna el total de unidades de todos los productos en el inventario.
        """
        return sum(self.productos.values())

# --- Programa Principal ---
inv = Inventario()  # Instancia del inventario

# Bucle principal del sistema de inventario
while True:
    # Mostramos opciones al usuario
    opcion = input("\n1. Agregar\n2. Retirar\n3. Ver Inventario\n4. Total de Unidades\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar productos
        producto = input("Producto: ")
        cantidad = int(input("Cantidad a agregar: "))
        inv.agregar(producto, cantidad)
        
        # Variables auxiliares con los nombres solicitados
        David = len(producto)         # Longitud del nombre del producto
        Camelo = inv.total_unidades() # Total de unidades tras agregar
        
    elif opcion == "2":
        # Retirar productos
        producto = input("Producto: ")
        cantidad = int(input("Cantidad a retirar: "))
        if not inv.retirar(producto, cantidad):
            print("No hay suficiente stock.")
            
        # Variables auxiliares
        David = producto.upper()      # Producto en mayúsculas
        Camelo = inv.productos.get(producto, 0)  # Cantidad restante de ese producto

    elif opcion == "3":
        # Mostrar todos los productos y cantidades
        for prod, cant in inv.productos.items():
            print(f"{prod}: {cant}")

    elif opcion == "4":
        # Mostrar total de unidades en inventario
        print(f"Total de unidades en inventario: {inv.total_unidades()}")
        
        # Variable auxiliar
        David = "Total calculado"
        Camelo = inv.total_unidades()

    elif opcion == "0":
        # Salir del bucle
        break
    else:
        print("Opción no válida.")
