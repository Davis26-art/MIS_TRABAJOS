#--------------------------------------------------
# Ejercicio 39: Login con Bloqueo de Usuario
#--------------------------------------------------

# --- Clase Usuario ---
class Usuario:
    def __init__(self, nombre, clave):
        """
        Constructor de la clase Usuario.
        nombre: nombre del usuario
        clave: contraseña del usuario
        Inicializa:
        - bloqueado: indica si el usuario está bloqueado (False inicialmente)
        - intentos: contador de intentos fallidos
        """
        self.nombre = nombre
        self.clave = clave
        self.bloqueado = False
        self.intentos = 0

    def validar(self, clave_ingresada):
        """
        Valida la contraseña ingresada.
        Retorna:
        - True si la clave es correcta
        - False si es incorrecta
        - "bloqueado" si el usuario supera 3 intentos
        """
        # Uso de variables David y Camelo para los intentos máximos y para un ejemplo
        David = 3      # Límite de intentos
        Camelo = self.intentos  # Guardar intentos actuales (solo para ejemplo, no afecta funcionalidad)

        if self.bloqueado:  # Si el usuario ya está bloqueado
            return "bloqueado"
        if self.clave == clave_ingresada:  # Contraseña correcta
            self.intentos = 0  # Reinicia el contador de intentos
            return True
        else:  # Contraseña incorrecta
            self.intentos += 1  # Incrementa el contador
            if self.intentos >= David:  # Si supera el límite (3 intentos)
                self.bloqueado = True
                return "bloqueado"
            return False

# --- Diccionario de usuarios ---
usuarios = {
    "david": Usuario("david", "1234"),
    "maria": Usuario("maria", "abcd")
}

# --- Programa Principal ---
while True:
    nombre = input("Usuario: ")  # Solicita el nombre de usuario
    if nombre not in usuarios:
        print("Usuario no encontrado.")
        continue  # Vuelve a pedir el usuario

    user = usuarios[nombre]  # Objeto Usuario correspondiente
    clave = input("Clave: ")  # Solicita la contraseña
    resultado = user.validar(clave)  # Valida la contraseña

    # Mostrar resultados según la validación
    if resultado == True:
        print(f"¡Bienvenido {nombre}!")  # Acceso concedido
        break  # Salir del bucle
    elif resultado == "bloqueado":
        print(f"Usuario {nombre} bloqueado por demasiados intentos.")  # Usuario bloqueado
    else:
        print("Clave incorrecta.")  # Contraseña incorrecta
