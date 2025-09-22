#--------------------------------------------------
# Ejercicio 3: Agenda de Contactos
#--------------------------------------------------

# --- Clase ---
class Contacto:  # Se define una clase llamada Contacto
    def __init__(self, David, Camelo):  # Constructor: inicializa los atributos
        self.nombre = David       # Guarda el nombre del contacto
        self.telefono = Camelo    # Guarda el teléfono del contacto

    def mostrar(self):  # Método que devuelve el contacto como un string bonito
        return f"{self.nombre} - {self.telefono}"

# --- Programa Principal ---
contactos = []  # Lista para guardar objetos Contacto
agenda = {}     # Diccionario para búsqueda rápida (clave = nombre, valor = teléfono)

while True:  # Bucle principal del programa
    opcion = input("\n1. Agregar contacto\n2. Buscar contacto\n3. Mostrar todos\n0. Salir\nOpción: ")

    if opcion == "1":  # --- Agregar contacto ---
        David = input("Nombre: ")
        Camelo = input("Teléfono: ")
        c = Contacto(David, Camelo)  # Creamos un objeto Contacto
        contactos.append(c)          # Lo agregamos a la lista
        agenda[David] = Camelo       # También lo guardamos en el diccionario

    elif opcion == "2":  # --- Buscar contacto ---
        David = input("Nombre a buscar: ")
        if David in agenda:  # Si el nombre está en el diccionario
            print(f"Teléfono de {David}: {agenda[David]}")
        else:
            print("No está en la agenda.")  # Si no existe, avisamos

    elif opcion == "3":  # --- Mostrar todos los contactos ---
        for c in contactos:        # Recorremos la lista de objetos Contacto
            print(c.mostrar())     # Usamos el método mostrar para imprimirlos

    elif opcion == "0":  # --- Salir ---
        break  # Rompe el bucle y termina el programa

    else:  # --- Opción inválida ---
        print("Opción no válida.")  # Si el usuario ingresa algo diferente a 0, 1, 2, 3
