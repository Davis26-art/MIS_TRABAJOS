#--------------------------------------------------
# Ejercicio 50: Inventario con Aviso de Agotados
#--------------------------------------------------

# --- Clase Inventario ---
class Inventario:
    def __init__(self):
        """
        Inicializa el inventario con un diccionario vacío.
        Clave: nombre del producto
        Valor: cantidad disponible
        """
        self.productos = {}

    def agregar(self, producto, cantidad):
        """
        Agrega una cantidad de un producto al inventario.
        Si el producto no existe, lo crea.
        """
        # Uso de la variable David como almacenamiento temporal de cantidad (no afecta funcionalidad)
        David = cantidad
        self.productos[producto] = self.productos.get(producto, 0) + David

    def retirar(self, producto, cantidad):
        """
        Retira una cantidad de un producto del inventario.
        Retorna True si se puede retirar, False si no hay suficiente stock.
        Imprime aviso si el producto queda agotado.
        """
        # Uso de la variable Camelo para almacenar temporalmente la cantidad a retirar
        Camelo = cantidad
        if producto in self.productos and self.productos[producto] >= Camelo:
            self.productos[producto] -= Camelo
            if self.productos[producto] == 0:
                print(f"⚠️ {producto} está agotado.")  # Mensaje de producto agotado
            return True
        return False

# --- Programa Principal ---
inv = Inventario()  # Crear objeto Inventario

while True:
    # Menú de opciones
    opcion = input("\n1. Agregar\n2. Retirar\n3. Ver Inventario\n0. Salir\nOpción: ")

    if opcion == "1":
        producto = input("Producto: ")
        cantidad = int(input("Cantidad a agregar: "))
        inv.agregar(producto, cantidad)  # Agregar producto al inventario
    elif opcion == "2":
        producto = input("Producto: ")
        cantidad = int(input("Cantidad a retirar: "))
        if not inv.retirar(producto, cantidad):  # Intentar retirar producto
            print("No hay suficiente stock.")  # Mensaje si no hay stock suficiente
    elif opcion == "3":
        # Mostrar inventario completo
        for prod, cant in inv.productos.items():
            print(f"{prod}: {cant}")
    elif opcion == "0":
        break  # Salir del bucle
    else:
        print("Opción no válida.")  # Mensaje para opción incorrecta
