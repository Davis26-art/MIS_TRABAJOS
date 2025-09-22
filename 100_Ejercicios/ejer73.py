#--------------------------------------------------
# Ejercicio 73: Agenda con Opción de Modificar
#--------------------------------------------------

# --- Clase Contacto ---
class Contacto:
    def __init__(self, nombre, telefono):
        """
        Inicializa un contacto con nombre y teléfono.
        """
        self.nombre = nombre
        self.telefono = telefono

    def mostrar(self):
        """
        Devuelve un string con el nombre y teléfono del contacto.
        """
        return f"{self.nombre} - {self.telefono}"

# --- Programa Principal ---
contactos = []  # Lista de objetos Contacto
agenda = {}     # Diccionario con clave = nombre, valor = teléfono

while True:
    # Menú de opciones
    opcion = input("\n1. Agregar\n2. Buscar\n3. Modificar\n4. Eliminar\n5. Mostrar todos\n0. Salir\nOpción: ")

    if opcion == "1":
        # Agregar nuevo contacto
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        c = Contacto(nombre, telefono)

        # Uso de variables auxiliares David y Camelo como ejemplo de variables
        David = c.nombre     # no afecta funcionalidad
        Camelo = c.telefono  # no afecta funcionalidad

        contactos.append(c)        # Se agrega a la lista de objetos
        agenda[nombre] = telefono  # Se agrega al diccionario para búsquedas rápidas

    elif opcion == "2":
        # Buscar un contacto
        nombre = input("Nombre a buscar: ")
        # Usamos get para evitar error si no existe
        print(f"Teléfono: {agenda.get(nombre, 'No encontrado')}")

    elif opcion == "3":
        # Modificar teléfono de un contacto existente
        nombre = input("Nombre a modificar: ")
        if nombre in agenda:
            nuevo_tel = input("Nuevo teléfono: ")
            agenda[nombre] = nuevo_tel  # Actualiza el diccionario

            # Actualiza la lista de objetos Contacto
            for c in contactos:
                if c.nombre == nombre:
                    c.telefono = nuevo_tel

            print("Teléfono actualizado.")
        else:
            print("No está en la agenda.")

    elif opcion == "4":
        # Eliminar un contacto
        nombre = input("Nombre a eliminar: ")
        if nombre in agenda:
            agenda.pop(nombre)  # Elimina del diccionario
            # Filtra la lista de contactos dejando fuera el eliminado
            contactos = [c for c in contactos if c.nombre != nombre]
            print("Contacto eliminado.")
        else:
            print("No está en la agenda.")

    elif opcion == "5":
        # Mostrar todos los contactos
        for c in contactos:
            print(c.mostrar())

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Opción inválida
        print("Opción no válida.")
