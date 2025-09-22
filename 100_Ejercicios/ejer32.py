#--------------------------------------------------
# Ejercicio 32: Inventario de Ropa con Descuento 
#--------------------------------------------------

# --- Clase ---
class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto.
        nombre: nombre del producto.
        precio: valor unitario del producto.
        cantidad: cantidad disponible en stock.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad):
        """
        Vende la cantidad indicada del producto si hay stock suficiente.
        Resta la cantidad vendida del stock.
        Retorna True si se pudo vender, False si no hay suficiente stock.
        """
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        return False

    def reabastecer(self, cantidad):
        """
        Agrega unidades al stock del producto.
        """
        self.cantidad += cantidad

    def mostrar_resumen(self):
        """
        Muestra el stock restante del producto.
        """
        print(f"{self.nombre} → Stock restante: {self.cantidad}")

# --- Programa Principal ---
# Lista de productos disponibles
productos = [
    Producto("Camiseta", 25000, 10),
    Producto("Pantalón", 60000, 5),
    Producto("Zapatos", 120000, 3)
]

# Diccionarios de ventas por persona
ventas_david = {}
ventas_camelo = {}

while True:
    persona = input("¿Quién hará la compra? (David/Camelo o 'fin' para salir): ").capitalize()
    if persona.lower() == "fin":
        break
    if persona not in ("David", "Camelo"):
        print("Nombre no válido. Elige David o Camelo.")
        continue

    # Mostrar inventario
    print("\nInventario de Ropa:")
    for i, p in enumerate(productos):
        print(f"{i+1}. {p.nombre} - ${p.precio} - Stock: {p.cantidad}")

    # Selección de producto
    opcion = int(input("Selecciona el producto (0 para cancelar): "))
    if opcion == 0:
        continue

    producto = productos[opcion-1]
    cantidad = int(input(f"¿Cuántos {producto.nombre} deseas comprar? "))

    # Intento de venta
    if producto.vender(cantidad):
        total = producto.precio * cantidad

        # Aplicar descuento si se compran más de 3 unidades
        if cantidad > 3:
            total *= 0.85  # 15% de descuento
            print("¡Descuento aplicado del 15%!")

        # Registrar la venta en el diccionario de la persona
        if persona == "David":
            ventas_david[producto.nombre] = ventas_david.get(producto.nombre, 0) + total
        else:
            ventas_camelo[producto.nombre] = ventas_camelo.get(producto.nombre, 0) + total

        print(f"Compra realizada por {persona}. Total: ${total}")
        producto.mostrar_resumen()
    else:
        print("No hay suficiente stock.")

# Mostrar resumen final de ventas
print("\nResumen de ventas de David:")
for nombre, total in ventas_david.items():
    print(f"{nombre}: ${total}")

print("\nResumen de ventas de Camelo:")
for nombre, total in ventas_camelo.items():
    print(f"{nombre}: ${total}")
