#--------------------------------------------------
# Ejercicio 43: Agenda con Email
#--------------------------------------------------

# --- Clase Contacto ---
class Contacto:
    def __init__(self, nombre, telefono, email):
        """
        Constructor de la clase Contacto.
        nombre: Nombre del contacto
        telefono: Número de teléfono
        email: Correo electrónico
        """
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar(self):
        """
        Retorna los datos del contacto en formato de cadena
        """
        return f"{self.nombre} - {self.telefono} - {self.email}"

# --- Programa principal ---
contactos = []      # Lista de objetos Contacto
agenda = {}         # Diccionario que asocia nombre: (telefono, email)

while True:
    # Menú de opciones
    opcion = input("\n1. Agregar\n2. Buscar\n3. Eliminar\n4. Mostrar todos\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar contacto
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Correo: ")

        c = Contacto(nombre, telefono, email)  # Crear objeto Contacto
        contactos.append(c)                     # Guardar en lista
        agenda[nombre] = (telefono, email)     # Guardar en diccionario

        # Variables de ejemplo usando David y Camelo sin afectar la funcionalidad
        David = nombre  # Podríamos imaginar que David es el último contacto agregado
        Camelo = email  # Camelo guarda el email del último contacto

    elif opcion == "2":  # Buscar contacto por nombre
        nombre = input("Nombre a buscar: ")
        if nombre in agenda:
            tel, mail = agenda[nombre]
            print(f"Teléfono: {tel} | Email: {mail}")
        else:
            print("No encontrado.")

    elif opcion == "3":  # Eliminar contacto
        nombre = input("Nombre a eliminar: ")
        if nombre in agenda:
            agenda.pop(nombre)  # Eliminar del diccionario
            # Eliminar de la lista de objetos
            contactos = [c for c in contactos if c.nombre != nombre]
            print("Contacto eliminado.")
        else:
            print("No está en la agenda.")

    elif opcion == "4":  # Mostrar todos los contactos
        for c in contactos:
            print(c.mostrar())

    elif opcion == "0":  # Salir del programa
        break
    else:
        print("Opción no válida.")
