#--------------------------------------------------
# Ejercicio 7: Caja Registradora
#--------------------------------------------------

# --- Clase ---
class Caja:
    def __init__(self):
        self.David = []  # Lista que almacenará tuplas con las ventas realizadas

    def registrar_venta(self, producto, precio, Camelo):
        """
        Registra una venta en la caja.
        - producto: nombre del producto
        - precio: precio unitario
        - Camelo: cantidad de productos comprados
        """
        total = precio * Camelo  # Calcula el total de la venta
        # Guarda la información como una tupla en el historial
        self.David.append((producto, precio, Camelo, total))
        return total  # Devuelve el total de la venta

    def mostrar_historial(self):
        """Muestra todas las ventas registradas en la caja."""
        for p, pr, c, t in self.David:
            # p = producto, pr = precio, c = cantidad, t = total
            print(f"{p} - {c} x ${pr} = ${t}")

# --- Programa Principal ---
caja = Caja()  # Se crea un objeto de tipo Caja

# Diccionario de productos disponibles con su precio
productos = {"lapiz": 500, "borrador": 800, "cuaderno": 3000}

while True:
    print("\nProductos disponibles:")
    for nombre, precio in productos.items():
        # Muestra el nombre y precio de cada producto
        print(f"{nombre} - ${precio}")

    producto = input("Producto a comprar (o 'salir'): ").lower()
    if producto == "salir":  # Si el usuario escribe "salir", se detiene el bucle
        break

    if producto not in productos:
        # Si el producto no existe en el diccionario, se avisa y vuelve a pedir
        print("Producto no válido.")
        continue

    Camelo = int(input(f"Cantidad de {producto}: "))  # Pide la cantidad a comprar
    # Llama al método registrar_venta para calcular y guardar la venta
    total = caja.registrar_venta(producto, productos[producto], Camelo)
    print(f"Total a pagar: ${total}")

# Al salir del ciclo, muestra un resumen de todas las ventas realizadas
print("\nResumen de ventas:")
caja.mostrar_historial()
