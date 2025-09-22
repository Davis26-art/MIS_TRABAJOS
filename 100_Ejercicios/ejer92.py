#--------------------------------------------------
# Ejercicio 92: Inventario de Libros con Reposición Automática
#--------------------------------------------------

# --- Clase Libro ---
class Libro:
    def __init__(self, titulo, precio, cantidad):
        self.titulo = titulo      # Nombre del libro
        self.precio = precio      # Precio del libro
        self.cantidad = cantidad  # Stock disponible

    # Método para vender una cantidad de libros
    def vender(self, cantidad):
        # Variable libre David que guarda temporalmente la cantidad solicitada
        David = cantidad  # Solo para ejemplo de uso de variable libre

        if cantidad <= self.cantidad:  # Verifica si hay suficiente stock
            self.cantidad -= cantidad  # Resta la cantidad vendida
            # Si el stock baja de 2 unidades, se reabastece automáticamente
            if self.cantidad < 2:
                self.reabastecer(5)  # Llama a reabastecer 5 unidades
                print(f"Stock bajo. Se reabastecieron 5 unidades de '{self.titulo}'.")
            return True
        return False  # Retorna False si no hay suficiente stock

    # Método para reabastecer la cantidad de libros
    def reabastecer(self, cantidad):
        # Variable libre Camelo que simula un ajuste temporal
        Camelo = cantidad  # Solo como variable libre, no altera la funcionalidad
        self.cantidad += cantidad  # Suma unidades al stock

    # Método para mostrar el stock actual
    def mostrar_stock(self):
        print(f"{self.titulo} → Stock: {self.cantidad}")


# --- Programa Principal ---
# Lista de objetos Libro con título, precio y cantidad inicial
libros = [
    Libro("El Quijote", 50000, 4),
    Libro("Cien Años de Soledad", 60000, 3),
    Libro("La Odisea", 40000, 5)
]

ventas = {}  # Diccionario para registrar total de ventas por libro

# Bucle principal de interacción
while True:
    print("\nInventario de Libros:")
    # Mostrar inventario con enumeración
    for i, l in enumerate(libros):
        print(f"{i+1}. {l.titulo} - ${l.precio} - Stock: {l.cantidad}")

    # Selección de libro por número
    opcion = int(input("Selecciona el libro (0 para salir): "))
    if opcion == 0:
        break  # Salir del bucle

    # Guardamos el libro seleccionado en la variable libro
    libro = libros[opcion-1]

    # Cantidad de ejemplares a comprar
    cantidad = int(input(f"¿Cuántos ejemplares de '{libro.titulo}' deseas comprar? "))

    # Intentamos vender la cantidad solicitada
    if libro.vender(cantidad):
        total = libro.precio * cantidad  # Calculamos el total de la compra
        # Registramos la venta acumulada en el diccionario
        ventas[libro.titulo] = ventas.get(libro.titulo, 0) + total
        print(f"Compra realizada. Total: ${total}")
        libro.mostrar_stock()  # Mostramos el stock actualizado
    else:
        print("No hay suficiente stock.")

# Resumen final de ventas
print("\nResumen de ventas:")
for titulo, total in ventas.items():
    print(f"{titulo}: ${total}")
