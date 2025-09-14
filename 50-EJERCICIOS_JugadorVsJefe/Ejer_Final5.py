#--------------------------------------------------
# EJERCICIO FINAL 5 -- Simulador de Tienda Online
#--------------------------------------------------

# Lista de productos en inventario: cada uno es un diccionario con nombre, precio y stock.
inventario = [
    {"nombre": "Camiseta", "precio": 25000, "cantidad": 5},
    {"nombre": "Pantalón", "precio": 80000, "cantidad": 3},
    {"nombre": "Zapatos", "precio": 120000, "cantidad": 2},
]

# Carrito de compras vacío al inicio.
carrito = []

print("🛒 Bienvenido a la Tienda Online")

while True:
    print("\nOpciones:")
    print("1) Ver inventario")
    print("2) Agregar producto al carrito")
    print("3) Ver carrito")
    print("4) Procesar pedido")
    print("q) Salir")
    opcion = input("Elige una opción: ").strip().lower()

    # Salir del sistema
    if opcion == "q":
        print("Gracias por visitarnos 👋")
        break

    # Mostrar inventario actual
    elif opcion == "1":
        print("\n📦 Inventario:")
        for i, producto in enumerate(inventario):
            print(f"{i+1}) {producto['nombre']} - ${producto['precio']} (Stock: {producto['cantidad']})")

    # Agregar producto al carrito
    elif opcion == "2":
        print("\n📦 Productos disponibles:")
        for i, producto in enumerate(inventario):
            print(f"{i+1}) {producto['nombre']} - ${producto['precio']} (Stock: {producto['cantidad']})")

        try:
            indice = int(input("Elige el número del producto: ")) - 1
            if indice < 0 or indice >= len(inventario):
                print("⚠ Producto no válido.")
                continue

            cantidad = int(input("Cantidad a agregar: "))
            if cantidad <= 0:
                print("⚠ Ingresa una cantidad mayor a 0.")
                continue

            # Verificamos si hay suficiente stock
            if cantidad > inventario[indice]["cantidad"]:
                print("⚠ No hay suficiente stock.")
            else:
                # Agregamos al carrito y reducimos stock temporalmente en inventario.
                carrito.append({"nombre": inventario[indice]["nombre"], 
                                "precio": inventario[indice]["precio"], 
                                "cantidad": cantidad})
                inventario[indice]["cantidad"] -= cantidad
                print("✅ Producto agregado al carrito.")

        except ValueError:
            print("⚠ Ingresa un número válido.")

    # Mostrar carrito
    elif opcion == "3":
        if not carrito:
            print("\n🛒 Tu carrito está vacío.")
        else:
            print("\n🛒 Carrito de compras:")
            total = 0
            for item in carrito:
                subtotal = item["precio"] * item["cantidad"]
                total += subtotal
                print(f"- {item['nombre']} x{item['cantidad']} = ${subtotal}")
            print(f"💰 Total actual: ${total}")

    # Procesar pedido
    elif opcion == "4":
        if not carrito:
            print("\n⚠ No tienes productos en el carrito.")
        else:
            print("\n💳 Procesando pedido...")
            total = 0
            for item in carrito:
                total += item["precio"] * item["cantidad"]
            print(f"✅ Pedido confirmado. Total a pagar: ${total}")
            carrito.clear()  # Vaciamos el carrito después de la compra
            print("🛍 ¡Gracias por tu compra!")

    # Si la opción no existe
    else:
        print("⚠ Opción no válida. Elige del 1 al 4 o q.")
