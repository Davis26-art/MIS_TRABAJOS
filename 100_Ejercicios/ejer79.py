#--------------------------------------------------
# Ejercicio 79: Gestión de Productos con Resumen Detallado
#--------------------------------------------------

# --- Clase Producto ---
class Producto:
    def __init__(self, nombre, precio):
        """
        Inicializa un producto con:
        - nombre: nombre del producto
        - precio: precio original del producto
        """
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        """
        Calcula y devuelve el precio final después de aplicar un descuento.
        - porcentaje: porcentaje de descuento a aplicar
        """
        return self.precio - (self.precio * porcentaje / 100)

# --- Programa Principal ---
productos = []          # Lista para almacenar objetos Producto
precios = {}            # Diccionario: nombre -> (precio original, descuento, precio final)

# Bucle principal para ingresar productos
while True:
    nombre = input("Producto (o 'fin'): ")
    if nombre.lower() == "fin":  # Condición de salida
        break

    # Entrada de datos
    precio = float(input("Precio: "))
    descuento = float(input("Descuento %: "))

    # Creación de objeto Producto
    p = Producto(nombre, precio)

    # Cálculo del precio final aplicando descuento
    precio_final = p.aplicar_descuento(descuento)

    # Agregar producto a la lista
    productos.append(p)

    # Guardar información en el diccionario precios
    precios[nombre] = (precio, descuento, precio_final)

    # Variables auxiliares con los nombres solicitados
    David = len(nombre)            # Longitud del nombre del producto
    Camelo = round(precio_final)   # Precio final redondeado

# --- Mostrar resumen ---
print("\nResumen de productos:")
for nombre, (precio, descuento, final) in precios.items():
    # Imprime cada producto con su precio original, descuento aplicado y precio final
    print(f"{nombre} | Original: ${precio:.2f} | Descuento: {descuento}% | Final: ${final:.2f}")
