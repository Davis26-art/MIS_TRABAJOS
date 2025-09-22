#--------------------------------------------------
# Ejercicio 13: Agenda de Contactos
#--------------------------------------------------

# --- Clase ---
class Contacto:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase Contacto.
        Guarda el nombre (David) y el teléfono (Camelo) de cada contacto.
        """
        self.David = David      # Atributo para almacenar el nombre
        self.Camelo = Camelo    # Atributo para almacenar el teléfono

    def mostrar(self):
        """
        Devuelve una cadena con el nombre y teléfono del contacto.
        """
        return f"{self.David} - {self.Camelo}"

# --- Programa Principal ---
contactos = []  # Lista que guarda objetos Contacto
agenda = {}     # Diccionario para búsquedas rápidas (clave = nombre, valor = teléfono)

while True:
    opcion = input("\n1. Agregar\n2. Buscar\n3. Eliminar\n4. Mostrar todos\n0. Salir\nOpción: ")

    if opcion == "1":  # Agregar un nuevo contacto
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        c = Contacto(nombre, telefono)  # Creamos un objeto Contacto
        contactos.append(c)              # Lo agregamos a la lista
        agenda[nombre] = telefono        # Lo agregamos al diccionario para búsqueda rápida

    elif opcion == "2":  # Buscar un contacto
        nombre = input("Nombre a buscar: ")
        # Usamos get para no generar error si no existe
        print(f"Teléfono: {agenda.get(nombre, 'No encontrado')}")

    elif opcion == "3":  # Eliminar un contacto
        nombre = input("Nombre a eliminar: ")
        if nombre in agenda:
            agenda.pop(nombre)  # Eliminamos del diccionario
            # Filtramos la lista de objetos para eliminar el contacto
            contactos = [c for c in contactos if c.David != nombre]
            print("Contacto eliminado.")
        else:
            print("No está en la agenda.")

    elif opcion == "4":  # Mostrar todos los contactos
        for c in contactos:
            print(c.mostrar())

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
