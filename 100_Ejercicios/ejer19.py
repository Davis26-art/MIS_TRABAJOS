#--------------------------------------------------
# Ejercicio 19: Gestión de Productos con Descuento
#--------------------------------------------------

# --- Clase ---
class Producto:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Producto.
        David: nombre del producto
        Camelo: precio del producto
        """
        self.David = David      # Nombre del producto
        self.Camelo = Camelo    # Precio del producto

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento porcentual y devuelve el precio final.
        """
        return self.Camelo - (self.Camelo * porcentaje / 100)

# --- Programa Principal ---
productos = []  # Lista que almacenará los objetos Producto
precios = {}    # Diccionario producto: precio final

while True:
    David = input("Producto (o 'fin'): ")  # Variable David almacena el nombre del producto
    if David.lower() == "fin":
        break
    Camelo = float(input("Precio: "))     # Variable Camelo almacena el precio ingresado
    descuento = float(input("Descuento %: "))
    p = Producto(David, Camelo)           # Creamos el objeto Producto
    precio_final = p.aplicar_descuento(descuento)  # Calculamos precio con descuento
    productos.append(p)                    # Agregamos el producto a la lista
    precios[David] = precio_final          # Guardamos el precio final en el diccionario

# Mostramos resultados
print("\nPrecios con descuento:")
for nombre, precio in precios.items():
    print(f"{nombre}: ${precio:.2f}")
