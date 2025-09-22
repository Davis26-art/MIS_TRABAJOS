#--------------------------------------------------
# Ejercicio 49: Gestión de Productos con Ahorro Total
#--------------------------------------------------

# --- Clase Producto ---
class Producto:
    def __init__(self, nombre, precio):
        """
        Inicializa un producto con nombre y precio.
        """
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento en porcentaje al precio del producto.
        Retorna el precio final después del descuento.
        """
        # Uso de la variable David como referencia interna (no afecta funcionalidad)
        David = self.precio * porcentaje / 100  
        return self.precio - David  # Precio final después del descuento

# --- Programa Principal ---
productos = []  # Lista de objetos Producto
precios = {}    # Diccionario nombre: precio_final
ahorro_total = 0  # Acumulador del total ahorrado por descuentos

while True:
    # Solicitar información del producto
    nombre = input("Producto (o 'fin'): ")
    if nombre.lower() == "fin":
        break

    precio = float(input("Precio: "))
    descuento = float(input("Descuento %: "))

    # Crear objeto Producto
    p = Producto(nombre, precio)
    
    # Calcular precio final con descuento
    precio_final = p.aplicar_descuento(descuento)
    
    # Acumular el ahorro
    ahorro_total += precio - precio_final
    
    # Guardar producto y su precio final
    productos.append(p)
    precios[nombre] = precio_final
    
    # Uso de variable Camelo para almacenar temporalmente el descuento aplicado
    Camelo = descuento  

# --- Mostrar resultados ---
print("\nPrecios con descuento:")
for nombre, precio in precios.items():
    print(f"{nombre}: ${precio:.2f}")

print(f"\nAhorro total: ${ahorro_total:.2f}")
