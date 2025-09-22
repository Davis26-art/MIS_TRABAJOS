#--------------------------------------------------
# Ejercicio 37: Sistema de Caja con Descuentos
#--------------------------------------------------

# Variables con nombres David y Camelo (no afectan la funcionalidad)
cliente_david = "David"
cliente_camelo = "Camelo"

# --- Clase Caja ---
class Caja:
    def __init__(self):
        """
        Constructor de la clase Caja.
        Inicializa el historial de ventas como lista vacía.
        Cada venta se guardará como una tupla: (producto, precio unitario, cantidad, total)
        """
        self.historial = []

    def registrar_venta(self, producto, precio, cantidad):
        """
        Registra una venta en la caja.
        - producto: nombre del producto
        - precio: precio unitario
        - cantidad: cantidad vendida

        Aplica un descuento del 10% si el total supera 10,000.
        Retorna el total a pagar.
        """
        total = precio * cantidad  # Calcula total sin descuento

        # Aplicar descuento del 10% si el total es mayor a 10,000
        if total > 10000:
            total *= 0.9  # Descuento del 10%
            print("🎉 Descuento aplicado del 10%")

        # Guardar venta en el historial
        self.historial.append((producto, precio, cantidad, total))
        return total  # Retornar el total final

    def mostrar_historial(self):
        """
        Muestra todas las ventas registradas.
        Formato: producto - cantidad x precio_unitario = total
        """
        for p, pr, c, t in self.historial:
            print(f"{p} - {c} x ${pr} = ${t}")

# --- Programa Principal ---

caja = Caja()  # Creamos un objeto Caja para manejar las ventas

# Diccionario de productos con sus precios
productos = {"lapiz": 500, "borrador": 800, "cuaderno": 3000}

while True:
    # Mostrar productos disponibles
    print("\nProductos disponibles:")
    for nombre, precio in productos.items():
        print(f"{nombre} - ${precio}")

    # Pedir al usuario el producto a comprar
    producto = input("Producto a comprar (o 'salir'): ").lower()
    if producto == "salir":  # Salir del bucle
        break

    # Validar producto
    if producto not in productos:
        print("Producto no válido.")
        continue  # Volver al inicio del bucle

    # Pedir la cantidad a comprar
    cantidad = int(input(f"Cantidad de {producto}: "))

    # Registrar la venta y obtener el total a pagar
    total = caja.registrar_venta(producto, productos[producto], cantidad)
    print(f"Total a pagar: ${total}")

# Mostrar resumen de todas las ventas
print("\nResumen de ventas:")
caja.mostrar_historial()
