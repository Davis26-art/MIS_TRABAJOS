#----------------------------------------------
# EJERCICIO 25 -- Sistema de inventario de productos
#----------------------------------------------

# Lista global para almacenar productos
inventario = []

def agregar_producto(nombre, categoria, precio, cantidad):
    """Agrega un nuevo producto al inventario"""
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"✔ Producto '{nombre}' agregado exitosamente")

def buscar_producto(nombre):
    """Busca un producto por nombre"""
    for i, producto in enumerate(inventario):
        if producto["nombre"].lower() == nombre.lower():
            return i  # Retorna la posición si lo encuentra
    return -1  # Si no existe

def actualizar_stock(nombre, cantidad):
    """Actualiza la cantidad de un producto"""
    posicion = buscar_producto(nombre)
    if posicion != -1:
        inventario[posicion]["cantidad"] += cantidad
        print(f"✔ Stock actualizado: {nombre} ahora tiene {inventario[posicion]['cantidad']} unidades")
    else:
        print(f"✘ Producto '{nombre}' no encontrado en el inventario")

def calcular_valor_total(nombre):
    """Calcula el valor total en stock de un producto"""
    posicion = buscar_producto(nombre)
    if posicion != -1:
        producto = inventario[posicion]
        total = producto["precio"] * producto["cantidad"]
        return round(total, 2)
    return None

def mostrar_inventario():
    """Muestra un reporte completo del inventario"""
    print("\n" + "="*50)
    print("REPORTE DE INVENTARIO")
    print("="*50)
    for producto in inventario:
        print(f"\nNombre: {producto['nombre']}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Precio unitario: ${producto['precio']}")
        print(f"Cantidad en stock: {producto['cantidad']}")
        print(f"Valor total: ${calcular_valor_total(producto['nombre'])}")
        print("-" * 30)


# Probando el sistema
print("SISTEMA DE INVENTARIO DE PRODUCTOS")

# Agregar productos
agregar_producto("Lápiz", "Papelería", 500, 100)
agregar_producto("Cuaderno", "Papelería", 2500, 50)
agregar_producto("Borrador", "Papelería", 800, 75)

# Actualizar stock
actualizar_stock("Cuaderno", 20)      # Aumenta stock
actualizar_stock("Marcador", 10)      # No existe

# Calcular valor total de un producto
print("\nValor total en stock de 'Lápiz':", calcular_valor_total("Lápiz"))

# Mostrar inventario completo
mostrar_inventario()
