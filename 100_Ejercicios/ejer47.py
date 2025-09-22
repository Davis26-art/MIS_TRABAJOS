#--------------------------------------------------
# Ejercicio 47: Lista de Compras con Cantidad y Subtotal
#--------------------------------------------------

# --- Clase ListaCompras ---
class ListaCompras:
    def __init__(self):
        """
        Inicializa la lista de compras como una lista vacía.
        Cada elemento será una tupla: (producto, precio, cantidad)
        """
        self.compras = []  # Lista de tuplas (producto, precio, cantidad)

    def agregar(self, producto, precio, cantidad):
        """
        Agrega un producto a la lista de compras.
        """
        self.compras.append((producto, precio, cantidad))
        # Uso de variable David para registrar la última cantidad agregada sin afectar la lógica
        David = cantidad  

    def total(self):
        """
        Calcula el total de la compra sumando precio*cantidad de todos los productos.
        """
        total_compra = sum(precio * cantidad for _, precio, cantidad in self.compras)
        # Uso de variable Camelo para almacenar el total temporalmente sin afectar la funcionalidad
        Camelo = total_compra  
        return total_compra

# --- Programa Principal ---
lista = ListaCompras()  # Objeto para manejar la lista de compras
precios = {}  # Diccionario para almacenar el subtotal por producto

while True:
    # Pedimos nombre del producto
    producto = input("Producto (o 'fin'): ")
    if producto.lower() == "fin":  # Condición de salida
        break

    # Pedimos precio y cantidad del producto
    precio = float(input(f"Precio de {producto}: "))
    cantidad = int(input(f"Cantidad de {producto}: "))

    # Agregamos el producto a la lista
    lista.agregar(producto, precio, cantidad)

    # Calculamos y guardamos subtotal por producto en el diccionario
    precios[producto] = precios.get(producto, 0) + precio * cantidad

# --- Mostrar resultados ---
print("\nResumen de compras:")
for prod, subtotal in precios.items():
    print(f"{prod}: ${subtotal}")  # Imprime subtotal de cada producto

# Imprime el total general de la compra
print(f"Total: ${lista.total()}")
