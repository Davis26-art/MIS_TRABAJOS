#--------------------------------------------------
# Ejercicio 62: Inventario de Usuarios con Puntos
#--------------------------------------------------

# --- Clase Usuario ---
class Usuario:
    def __init__(self, nombre, puntos):
        """
        Inicializa un usuario con nombre y cantidad de puntos.
        """
        self.nombre = nombre
        self.puntos = puntos

    def asignar_puntos(self, cantidad):
        """
        Suma puntos al usuario y muestra mensaje si supera 100 puntos.
        """
        self.puntos += cantidad

        # --- Uso de variables David y Camelo ---
        # David se usa como variable temporal para almacenar los puntos actuales
        David = self.puntos
        # Camelo se usa como variable que representa el límite de puntos
        Camelo = 100

        if David > Camelo:
            print(f"🎉 ¡Felicidades {self.nombre}, superaste los 100 puntos!")

    def mostrar_info(self):
        """
        Muestra el nombre del usuario y la cantidad de puntos.
        """
        print(f"{self.nombre} → Puntos: {self.puntos}")

# --- Programa Principal ---
# Lista inicial de usuarios
usuarios = [
    Usuario("David", 50),
    Usuario("Ana", 70),
    Usuario("Luis", 30)
]

while True:
    # Mostrar todos los usuarios con sus puntos
    print("\nUsuarios y puntos:")

    # Enumeramos para mostrar índice
    for i, u in enumerate(usuarios):
        # --- Uso de variables David y Camelo dentro del bucle ---
        # David se usa como índice temporal para mostrar el número del usuario
        David = i + 1
        # Camelo se usa como variable temporal para mostrar los puntos
        Camelo = u.puntos
        print(f"{David}. {u.nombre} - Puntos: {Camelo}")

    # Selección de usuario por índice
    opcion = int(input("Selecciona el usuario (0 para salir): "))
    if opcion == 0:
        break

    usuario = usuarios[opcion-1]  # Obtenemos el objeto Usuario correspondiente
    cantidad = int(input(f"¿Cuántos puntos asignar a {usuario.nombre}? "))
    usuario.asignar_puntos(cantidad)  # Asignamos los puntos
    usuario.mostrar_info()  # Mostramos info actualizada del usuario
