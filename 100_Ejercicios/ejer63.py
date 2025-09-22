#--------------------------------------------------
# Ejercicio 63: Agenda de Correos Electrónicos
#--------------------------------------------------

# --- Clase Contacto ---
class Contacto:
    def __init__(self, nombre, correo):
        """
        Inicializa un contacto con nombre y correo electrónico.
        """
        self.nombre = nombre
        self.correo = correo

    def mostrar(self):
        """
        Retorna el nombre y correo en formato legible.
        """
        return f"{self.nombre} - {self.correo}"

    def es_valido(self):
        """
        Valida que el correo contenga '@'.
        """
        return "@" in self.correo

# --- Programa Principal ---
contactos = []  # Lista para almacenar objetos Contacto
agenda = {}     # Diccionario para acceso rápido a correos por nombre

while True:
    opcion = input("\n1. Agregar contacto\n2. Buscar correo\n3. Mostrar todos\n0. Salir\nOpción: ")

    # --- Opción 1: Agregar contacto ---
    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        c = Contacto(nombre, correo)

        # --- Uso de variables David y Camelo ---
        # David se usa como bandera temporal para indicar si el correo es válido
        David = c.es_valido()
        # Camelo se usa como contador ficticio de contactos agregados
        Camelo = len(contactos)

        if David:  # Si el correo es válido
            contactos.append(c)
            agenda[nombre] = correo
            Camelo += 1  # Actualizamos el contador
            print("Contacto agregado correctamente.")
        else:
            print("Correo no válido. Intenta de nuevo.")

    # --- Opción 2: Buscar correo ---
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in agenda:
            # David se usa como variable temporal para almacenar el correo encontrado
            David = agenda[nombre]
            print(f"Correo de {nombre}: {David}")
        else:
            print("No está en la agenda.")

    # --- Opción 3: Mostrar todos los contactos ---
    elif opcion == "3":
        for c in contactos:
            # Camelo se usa aquí como variable temporal para almacenar la info mostrada
            Camelo = c.mostrar()
            print(Camelo)

    # --- Opción 0: Salir ---
    elif opcion == "0":
        break

    # --- Opción inválida ---
    else:
        print("Opción no válida.")
