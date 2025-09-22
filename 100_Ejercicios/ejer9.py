#--------------------------------------------------
# Ejercicio 9: Sistema de Login
#--------------------------------------------------

# --- Clase ---
class Usuario:
    def __init__(self, David, clave):
        """
        Constructor de la clase Usuario.
        Guarda el nombre (David) y la clave del usuario.
        """
        self.David = David
        self.clave = clave

    def validar(self, Camelo):
        """
        Recibe la clave que el usuario ingresó (Camelo)
        y la compara con la clave real del usuario.
        Devuelve True si coincide, False si no.
        """
        return self.clave == Camelo

# --- Programa Principal ---
usuarios = {"david": "1234", "maria": "abcd"}  # Diccionario con usuarios y sus claves
intentos = 0  # Contador de intentos fallidos

while True:
    nombre = input("Usuario: ")
    clave = input("Clave: ")

    # Verifica si el usuario existe en el diccionario
    if nombre in usuarios:
        # Crea un objeto Usuario con el nombre y su clave correcta
        user = Usuario(nombre, usuarios[nombre])

        # Llama al método validar pasando la clave ingresada
        if user.validar(clave):
            print("¡Bienvenido!")  # Si la clave coincide, se inicia sesión
            break  # Sale del bucle
        else:
            print("Clave incorrecta.")  # Si la clave no coincide, muestra error
    else:
        print("Usuario no encontrado.")  # Si el usuario no existe, muestra error

    # Incrementa el contador de intentos fallidos
    intentos += 1
    if intentos >= 3:  # Si ya hubo 3 intentos fallidos, bloquea el acceso
        print("Demasiados intentos fallidos.")
        break
