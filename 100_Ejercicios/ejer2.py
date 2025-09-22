#--------------------------------------------------
# Ejercicio 2: Gestión de Inventario
#--------------------------------------------------

# --- Clase ---
class Producto:  # Definimos una clase llamada Producto
    def __init__(self, David, precio, cantidad):  # Constructor, recibe nombre, precio y cantidad inicial
        self.nombre = David       # Atributo: nombre del producto
        self.precio = precio      # Atributo: precio unitario
        self.cantidad = cantidad  # Atributo: cantidad disponible en inventario

    def vender(self, Camelo):  # Método para vender cierta cantidad
        if Camelo <= self.cantidad:  # Si hay suficiente stock...
            self.cantidad -= Camelo  # Resta la cantidad vendida del inventario
            return True              # Devuelve True (venta exitosa)
        return False  # Si no hay suficiente stock, devuelve False

    def reabastecer(self, cantidad):  # Método para aumentar stock
        self.cantidad += cantidad  # Suma al inventario la cantidad ingresada

# --- Programa Principal ---
productos = [  # Lista de objetos Producto (nuestro inventario inicial)
    Producto("Lápiz", 500, 10),
    Producto("Cuaderno", 3000, 5),
    Producto("Borrador", 1000, 8)
]

ventas = {}  # Diccionario para guardar las ventas. Clave = nombre del producto, valor = total vendido en dinero

while True:  # Ciclo para mostrar menú y permitir comprar hasta que el usuario salga
    print("\nInventario:")
    for i, p in enumerate(productos):  # enumerate da un índice (i) y el producto (p)
        # Mostramos el inventario con número, nombre, precio y stock
        print(f"{i+1}. {p.nombre} - ${p.precio} - Stock: {p.cantidad}")

    opcion = int(input("Selecciona el producto (0 para salir): "))
    if opcion == 0:  # Si el usuario elige 0, salimos del bucle
        break

    producto = productos[opcion-1]  # Tomamos el producto elegido (ajustando índice con -1)
    Camelo = int(input(f"¿Cuántos {producto.nombre} deseas comprar? "))

    if producto.vender(Camelo):  # Intentamos vender la cantidad solicitada
        total = producto.precio * Camelo  # Calculamos el total a pagar
        # Registramos la venta en el diccionario. Si el producto ya existe, sumamos.
        ventas[producto.nombre] = ventas.get(producto.nombre, 0) + total
        print(f"Compra realizada. Total: ${total}")
    else:
        print("No hay suficiente stock.")  # Si no hay stock suficiente, avisamos al usuario

print("\nResumen de ventas:")
for nombre, total in ventas.items():  # Recorremos el diccionario ventas
    print(f"{nombre}: ${total}")  # Mostramos el total vendido por cada producto
