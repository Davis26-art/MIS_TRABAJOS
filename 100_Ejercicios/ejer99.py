#--------------------------------------------------
# Ejercicio 99: Login con Recuperación de Clave
#--------------------------------------------------

import random  # Para generar claves temporales aleatorias
import string  # Para caracteres alfanuméricos en la clave

# --- Clase Usuario ---
class Usuario:
    def __init__(self, nombre, clave):
        self.nombre = nombre  # Almacena el nombre del usuario
        self.clave = clave    # Almacena la clave del usuario

    # Método para validar si la clave ingresada coincide
    def validar(self, clave_ingresada):
        # Variable libre David que almacena temporalmente la clave ingresada
        David = clave_ingresada
        return self.clave == David

    # Método para generar una clave temporal aleatoria
    def generar_clave_temporal(self):
        # Variable libre Camelo que almacena temporalmente la clave generada
        Camelo = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.clave = Camelo  # Se asigna la clave temporal al usuario
        return Camelo

# Diccionario inicial de usuarios con su nombre como clave
usuarios = {
    "david": Usuario("david", "1234"),
    "maria": Usuario("maria", "abcd")
}

# --- Programa Principal ---
while True:
    # Menú principal
    opcion = input("\n1. Iniciar sesión\n2. Recuperar clave\n0. Salir\nOpción: ")

    if opcion == "0":  # Salir del programa
        break

    elif opcion == "1":  # Opción de iniciar sesión
        nombre = input("Usuario: ")
        clave = input("Clave: ")

        # Comprobación: si existe el usuario y la clave es correcta
        if nombre in usuarios and usuarios[nombre].validar(clave):
            print("¡Bienvenido!")
            break  # Salir del bucle tras login exitoso
        else:
            print("Usuario o clave incorrecta.")

    elif opcion == "2":  # Opción de recuperar clave
        nombre = input("Usuario para recuperar: ")
        if nombre in usuarios:
            # Se genera y asigna una clave temporal
            nueva = usuarios[nombre].generar_clave_temporal()
            print(f"Clave temporal generada: {nueva} (úsala para iniciar sesión)")
        else:
            print("Usuario no encontrado.")

    else:
        print("Opción no válida.")  # Manejo de opción inválida
