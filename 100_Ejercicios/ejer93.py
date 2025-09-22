#--------------------------------------------------
# Ejercicio 93: Agenda de Cumpleaños
#--------------------------------------------------

from datetime import datetime  # Importamos datetime para manejar fechas

# --- Clase Contacto ---
class Contacto:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre  # Nombre de la persona
        self.dia = dia        # Día de cumpleaños
        self.mes = mes        # Mes de cumpleaños

    # Método para mostrar el cumpleaños
    def mostrar(self):
        return f"{self.nombre} - Cumpleaños: {self.dia}/{self.mes}"

    # Método para verificar si el cumpleaños es este mes
    def es_cumple_mes(self):
        mes_actual = datetime.now().month  # Obtenemos el mes actual
        return self.mes == mes_actual      # Retorna True si coincide con el mes actual

# --- Programa Principal ---
contactos = []  # Lista para almacenar objetos Contacto
agenda = {}     # Diccionario para acceso rápido: nombre -> "día/mes"

while True:
    opcion = input("\n1. Agregar cumpleaños\n2. Buscar cumpleaños\n3. Mostrar todos\n0. Salir\nOpción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        dia = int(input("Día de cumpleaños: "))
        mes = int(input("Mes de cumpleaños (número): "))

        # Variables libres: David y Camelo
        David = nombre  # Solo como variable libre, no afecta la funcionalidad
        Camelo = dia    # Otra variable libre para mostrar su uso temporal

        # Creamos objeto Contacto y lo agregamos a la lista
        c = Contacto(nombre, dia, mes)
        contactos.append(c)
        # Agregamos a la agenda para búsqueda rápida
        agenda[nombre] = f"{dia}/{mes}"

        # Verificamos si el cumpleaños es este mes
        if c.es_cumple_mes():
            print(f"🎉 ¡{nombre} cumple este mes!")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        # Buscamos en el diccionario agenda
        if nombre in agenda:
            print(f"Cumpleaños de {nombre}: {agenda[nombre]}")
        else:
            print("No está en la agenda.")

    elif opcion == "3":
        # Mostramos todos los contactos usando el método mostrar()
        for c in contactos:
            print(c.mostrar())

    elif opcion == "0":
        break  # Salir del bucle

    else:
        print("Opción no válida.")
