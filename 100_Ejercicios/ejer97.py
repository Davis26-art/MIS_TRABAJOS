#--------------------------------------------------
# Ejercicio 97: Sistema de Gestión de Inventario de Ropa
#--------------------------------------------------

# --- Clase Caja ---
class Caja:
    def __init__(self):
        # Lista para guardar el historial de ventas
        self.historial = []

        # Inventario con cada producto: [precio, stock]
        self.inventario = {"camiseta": [20000, 5],
                           "pantalon": [35000, 3],
                           "chaqueta": [50000, 2]}

    # Método para registrar ventas
    def registrar_venta(self, producto, cantidad):
        precio, stock = self.inventario[producto]  # Desempaqueta precio y stock
        if cantidad > stock:                        # Verifica si hay suficiente stock
            print("No hay suficiente stock.")
            return 0
        # Actualiza el stock restando la cantidad vendida
        self.inventario[producto][1] -= cantidad

        # Calcula el total de la venta
        total = precio * cantidad

        # Variables libres para mostrar uso sin afectar la funcionalidad
        David = producto   # David almacena temporalmente el nombre del producto
        Camelo = total     # Camelo almacena temporalmente el total de la venta

        # Agrega la venta al historial: (producto, precio, cantidad, total)
        self.historial.append((producto, precio, cantidad, total))
        return total

    # Método para reabastecer un producto
    def reabastecer(self, producto, cantidad):
        if producto in self.inventario:
            # Incrementa el stock del producto
            self.inventario[producto][1] += cantidad
            print(f"Reabastecido {producto}. Stock actual: {self.inventario[producto][1]}")
        else:
            print("Producto no existe.")

    # Método para mostrar el historial de ventas
    def mostrar_historial(self):
        for p, pr, c, t in self.historial:
            print(f"{p} - {c} x ${pr} = ${t}")

# --- Programa Principal ---
caja = Caja()  # Instancia del sistema de caja

while True:
    # Muestra el inventario actual
    print("\nInventario:")
    for nombre, datos in caja.inventario.items():
        print(f"{nombre} - ${datos[0]} - Stock: {datos[1]}")

    # Menú de opciones
    opcion = input("1. Comprar | 2. Reabastecer | 0. Salir: ")

    if opcion == "0":  # Salir del programa
        break
    elif opcion == "1":  # Comprar producto
        producto = input("Producto a comprar: ").lower()
        if producto not in caja.inventario:
            print("Producto no válido.")
            continue

        cantidad = int(input(f"Cantidad de {producto}: "))
        total = caja.registrar_venta(producto, cantidad)
        if total > 0:
            print(f"Total a pagar: ${total}")
    elif opcion == "2":  # Reabastecer producto
        producto = input("Producto a reabastecer: ").lower()
        cantidad = int(input(f"Cantidad a agregar: "))
        caja.reabastecer(producto, cantidad)
    else:
        print("Opción no válida.")

# Muestra el resumen final de ventas
print("\nResumen de ventas:")
caja.mostrar_historial()
