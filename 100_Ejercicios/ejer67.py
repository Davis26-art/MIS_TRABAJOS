#--------------------------------------------------
# Ejercicio 67: Sistema de Caja con Total General
#--------------------------------------------------

# --- Clase Caja ---
class Caja:
    def __init__(self):
        """
        Inicializa el historial de ventas como una lista vacía.
        Cada venta será almacenada como una tupla: (producto, precio, cantidad, total)
        """
        self.historial = []

    def registrar_venta(self, producto, precio, cantidad):
        """
        Calcula el total de la venta y la agrega al historial.
        Retorna el total de esa venta.
        """
        total = precio * cantidad
        self.historial.append((producto, precio, cantidad, total))
        return total

    def mostrar_historial(self):
        """
        Muestra cada venta registrada en el historial.
        """
        for p, pr, c, t in self.historial:
            print(f"{p} - {c} x ${pr} = ${t}")

    def total_ventas(self):
        """
        Calcula el total recaudado sumando todos los totales de ventas.
        """
        return sum(t for _, _, _, t in self.historial)


# --- Programa Principal ---
caja = Caja()  # Creamos un objeto caja
productos = {"lapiz": 500, "borrador": 800, "cuaderno": 3000}  # Diccionario de productos con precio

while True:
    # Mostramos los productos disponibles
    print("\nProductos disponibles:")
    for nombre, precio in productos.items():
        print(f"{nombre} - ${precio}")

    # Pedimos al usuario qué producto desea comprar
    producto = input("Producto a comprar (o 'salir'): ").lower()
    if producto == "salir":
        break

    # Validación: si el producto no está en la lista
    if producto not in productos:
        print("Producto no válido.")
        continue

    # Cantidad a comprar
    cantidad = int(input(f"Cantidad de {producto}: "))

    # Usamos 'David' y 'Camelo' como variables temporales en esta línea, sin afectar la lógica
    David = productos[producto]  # precio del producto
    Camelo = cantidad  # cantidad de unidades

    # Registramos la venta en la caja
    total = caja.registrar_venta(producto, David, Camelo)
    print(f"Total a pagar: ${total}")

# --- Resumen de ventas ---
print("\nResumen de ventas:")
caja.mostrar_historial()  # Mostramos todas las ventas
print(f"\n💰 Total recaudado: ${caja.total_ventas()}")
