# Este es el nombre del archivo donde se van a guardar los contactos
archivo_agenda = "agenda.txt"

# 💡 Este bloque se encarga de ponerle un encabezado bonito al archivo si no lo tiene aún
with open(archivo_agenda, "r", encoding='utf-8') as f:
    contenido = f.readlines()  # lee todo el contenido del archivo en una lista

# Si el archivo está vacío o no tiene "AGENDA DE CONTACTOS", le metemos el título y una tablita
if not contenido or "AGENDA DE CONTACTOS" not in contenido[0]:
    encabezado = [
        "==============================\n",
        "       AGENDA DE CONTACTOS\n",
        "==============================\n",
        "|     NOMBRE     |  TELÉFONO   |\n",
        "------------------------------\n"
    ]
    contenido = encabezado + contenido  # pegamos el encabezado arriba del contenido actual
    with open(archivo_agenda, "w", encoding='utf-8') as f:
        f.writelines(contenido)  # volvemos a guardar todo en el archivo
    print("Título agregado a la agenda.")  # mensaje para saber que se hizo
else:
    print("La agenda ya tiene un título.")  # si ya lo tenía, no hace nada

# ----------------- FUNCIONES -----------------

# Muestra el menú de opciones cada vez que se repite el programa
def mostrar_menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Ver contactos")
    print("2. Agregar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

# Muestra en pantalla todos los contactos guardados
def ver_contactos():
    print("\n--- Contactos ---")
    with open(archivo_agenda, "r", encoding='utf-8') as f:
        for linea in f:
            print(linea.strip())  # strip() es para quitar los saltos de línea

# Permite agregar un nuevo contacto al archivo
def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    # Se guarda en formato tipo tabla, bien organizadito
    with open(archivo_agenda, "a", encoding='utf-8') as f:
        f.write(f"| {nombre:<13} | {telefono:<11} |\n")  # <13 y <11 son espacios para que se alineen bonito
    print("Contacto agregado.")

# Permite modificar un contacto si el nombre coincide
def modificar_contacto():
    nombre = input("Nombre del contacto a modificar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_tel = input("Nuevo teléfono: ")

    # Primero se lee todo el archivo
    with open(archivo_agenda, "r", encoding='utf-8') as f:
        lineas = f.readlines()

    # Luego se vuelve a escribir, haciendo el cambio donde corresponde
    with open(archivo_agenda, "w", encoding='utf-8') as f:
        for linea in lineas:
            # Si encuentra una línea que empieza con ese nombre, la reemplaza
            if linea.strip().startswith(f"| {nombre}"):
                f.write(f"| {nuevo_nombre:<13} | {nuevo_tel:<11} |\n")
            else:
                f.write(linea)  # Si no es esa línea, la deja igual
    
    print("Contacto modificado.")

# Permite eliminar un contacto por nombre
def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")

    # Leemos todo el archivo
    with open(archivo_agenda, "r", encoding='utf-8') as f:
        lineas = f.readlines()

    # Reescribimos el archivo, dejando fuera el contacto que queremos eliminar
    with open(archivo_agenda, "w", encoding='utf-8') as f:
        for linea in lineas:
            # Solo escribimos las líneas que no empiecen con ese nombre
            if not linea.strip().startswith(f"| {nombre}"):
                f.write(linea)

    print("Contacto eliminado.")

# ----------------- MENÚ PRINCIPAL -----------------

# Este es el corazón del programa, se repite hasta que elijas salir
while True:
    mostrar_menu()  # Mostramos el menú de opciones
    opcion = input("Opción (1-5): ")  # El usuario elige una opción

    if opcion == "1":
        ver_contactos()
    elif opcion == "2":
        agregar_contacto()
    elif opcion == "3":
        modificar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo...")  # Terminamos el programa
        break
    else:
        print("Opción no válida.")  # Por si alguien escribe otra cosa que no sea del 1 al 5
