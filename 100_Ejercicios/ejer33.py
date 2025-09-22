#--------------------------------------------------
# Ejercicio 33: Agenda con Eliminación de Contactos
#--------------------------------------------------

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar(self):
        return f"{self.nombre} - {self.telefono}"

    def eliminar(self):
        print(f"Contacto '{self.nombre}' eliminado.")

# --- Programa Principal ---
# Cada persona tendrá su propia agenda
agenda_david = []
agenda_camelo = []

# Diccionarios de apoyo para búsqueda rápida
contactos_david = {}
contactos_camelo = {}

while True:
    persona = input("¿Quién está usando la agenda? (David/Camelo o 'fin' para salir): ").capitalize()
    if persona.lower() == "fin":
        break
    if persona not in ("David", "Camelo"):
        print("Nombre no válido. Elige David o Camelo.")
        continue

    # Selección de la agenda según la persona
    if persona == "David":
        agenda = agenda_david
        contactos = contactos_david
    else:
        agenda = agenda_camelo
        contactos = contactos_camelo

    opcion = input("\n1. Agregar contacto\n2. Buscar contacto\n3. Mostrar todos\n4. Eliminar contacto\n0. Salir\nOpción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        c = Contacto(nombre, telefono)
        agenda.append(c)
        contactos[nombre] = telefono

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in contactos:
            print(f"Teléfono de {nombre}: {contactos[nombre]}")
        else:
            print("No está en la agenda.")

    elif opcion == "3":
        if not agenda:
            print("La agenda está vacía.")
        for c in agenda:
            print(c.mostrar())

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if nombre in contactos:
            contactos.pop(nombre)
            agenda = [c for c in agenda if c.nombre != nombre]
            Contacto(nombre, "").eliminar()
        else:
            print("No se encontró el contacto.")

    elif opcion == "0":
        break

    else:
        print("Opción no válida.")
