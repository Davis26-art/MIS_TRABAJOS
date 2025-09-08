# ============================
# AGENDA DE CONTACTOS
# ============================

# Archivo donde se guardarán los contactos
archivo_agenda = "agenda.txt"

# ----------------------------
# ENCABEZADO DE LA AGENDA
# ----------------------------
# Si el archivo no tiene título, se lo agregamos
with open(archivo_agenda, "r", encoding="utf-8") as f:
    contenido = f.readlines()

if not contenido or "AGENDA DE CONTACTOS" not in contenido[0]:
    encabezado = [
        "==============================\n",
        "       AGENDA DE CONTACTOS\n",
        "==============================\n",
        "|     NOMBRE     |  TELÉFONO   |\n",
        "------------------------------\n"
    ]
    contenido = encabezado + contenido
    with open(archivo_agenda, "w", encoding="utf-8") as f:
        f.writelines(contenido)
    print("Título agregado a la agenda.")
else:
    print("La agenda ya tiene un título.")

# ----------------------------
# FUNCIONES
# ----------------------------

def mostrar_menu():
    """Muestra las opciones del menú principal"""
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Ver contactos")
    print("2. Agregar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def ver_contactos():
    """Muestra todos los contactos almacenados"""
    print("\n--- Contactos ---")
    with open(archivo_agenda, "r", encoding="utf-8") as f:
        for linea in f:
            print(linea.strip())

def agregar_contacto():
    """Agrega un nuevo contacto a la agenda"""
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    with open(archivo_agenda, "a", encoding="utf-8") as f:
        f.write(f"| {nombre:<13} | {telefono:<11} |\n")
    print("Contacto agregado.")

def modificar_contacto():
    """Modifica un contacto existente"""
    nombre = input("Nombre del contacto a modificar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_tel = input("Nuevo teléfono: ")

    with open(archivo_agenda, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    with open(archivo_agenda, "w", encoding="utf-8") as f:
        for linea in lineas:
            if linea.strip().startswith(f"| {nombre}"):
                f.write(f"| {nuevo_nombre:<13} | {nuevo_tel:<11} |\n")
            else:
                f.write(linea)

    print("Contacto modificado.")

def eliminar_contacto():
    """Elimina un contacto de la agenda"""
    nombre = input("Nombre del contacto a eliminar: ")

    with open(archivo_agenda, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    with open(archivo_agenda, "w", encoding="utf-8") as f:
        for linea in lineas:
            if not linea.strip().startswith(f"| {nombre}"):
                f.write(linea)

    print("Contacto eliminado.")

# ----------------------------
# MENÚ PRINCIPAL
# ----------------------------
while True:
    mostrar_menu()
    opcion = input("Opción (1-5): ")

    if opcion == "1":
        ver_contactos()
    elif opcion == "2":
        agregar_contacto()
    elif opcion == "3":
        modificar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
