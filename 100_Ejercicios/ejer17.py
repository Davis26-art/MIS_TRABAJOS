#--------------------------------------------------
# Ejercicio 17: Lista de Compras con Diccionario
#--------------------------------------------------

# --- Clase ---
class ListaCompras:
    def __init__(self):
        """
        Constructor de la clase ListaCompras.
        self.David: lista que guarda tuplas (producto, precio)
        """
        self.David = []  # Lista de tuplas (producto, precio)

    def agregar(self, Camelo, precio):
        """
        Agrega un producto y su precio a la lista.
        Camelo: nombre del producto
        precio: valor del producto
        """
        self.David.append((Camelo, precio))

    def total(self):
        """
        Calcula el total sumando los precios de todos los productos en la lista.
        """
        return sum(precio for _, precio in self.David)

# --- Programa Principal ---
lista = ListaCompras()  # Creamos el objeto lista de compras
precios = {}             # Diccionario producto: precio

while True:
    David = input("Producto (o 'fin'): ")  # Variable David almacena el nombre del producto
    if David.lower() == "fin":             # Si escribe "fin", termina el bucle
        break
    Camelo = float(input(f"Precio de {David}: "))  # Precio ingresado para el producto
    lista.agregar(David, Camelo)                   # Agregamos a la lista
    precios[David] = Camelo                        # Guardamos en el diccionario

# Mostramos resumen de compras
print("\nResumen de compras:")
for prod, precio in precios.items():
    print(f"{prod}: ${precio}")

# Mostramos total
print(f"Total: ${lista.total()}")
