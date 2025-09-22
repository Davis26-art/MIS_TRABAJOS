#--------------------------------------------------
# Ejercicio 69: Login con Registro de Usuario
#--------------------------------------------------

# --- Clase Usuario ---
class Usuario:
    def __init__(self, nombre, clave):
        """
        Inicializa un usuario con su nombre y clave.
        """
        self.nombre = nombre
        self.clave = clave

    def validar(self, clave_ingresada):
        """
        Compara la clave ingresada con la almacenada y devuelve True si coinciden.
        """
        return self.clave == clave_ingresada


# --- Programa Principal ---
# Diccionario con usuarios ya registrados
usuarios = {"david": "1234", "maria": "abcd"}

while True:
    # Mostramos las opciones al usuario
    opcion = input("\n1. Iniciar sesión\n2. Crear usuario\n0. Salir\nOpción: ")
    
    # Salir del programa
    if opcion == "0":
        break

    # Iniciar sesión
    elif opcion == "1":
        nombre = input("Usuario: ")
        clave = input("Clave: ")

        # Uso de variables 'David' y 'Camelo' como temporales dentro del flujo
        David = nombre   # Podría representar usuario temporal
        Camelo = clave   # Podría representar clave temporal

        # Verificamos si el usuario existe
        if David in usuarios:
            user = Usuario(David, usuarios[David])
            if user.validar(Camelo):
                print("¡Bienvenido!")
                break
            else:
                print("Clave incorrecta.")
        else:
            print("Usuario no encontrado.")

    # Crear un nuevo usuario
    elif opcion == "2":
        nuevo_nombre = input("Nuevo usuario: ")
        if nuevo_nombre in usuarios:
            print("Ese usuario ya existe.")
        else:
            nueva_clave = input("Crea una clave: ")
            usuarios[nuevo_nombre] = nueva_clave
            print("Usuario creado exitosamente.")

    # Opción no válida
    else:
        print("Opción no válida.")
