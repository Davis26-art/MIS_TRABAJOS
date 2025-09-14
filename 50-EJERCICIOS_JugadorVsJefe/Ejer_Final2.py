#--------------------------------------------------
# EJERCICIO FINAL 2 -- Gestor de Biblioteca
#--------------------------------------------------

# Listas vacías para almacenar datos. Cada elemento será un diccionario simple.
libros = []       # Guardará {"titulo":..., "autor":..., "id":...}
usuarios = []     # Guardará {"nombre":..., "id":...}
prestamos = []    # Guardará {"id_libro":..., "id_usuario":..., "fecha":...}

print("📚 Gestor de Biblioteca")

while True:
    # Menú principal: permite elegir qué hacer.
    print("\nOpciones:")
    print("1) Registrar libro")
    print("2) Registrar usuario")
    print("3) Registrar préstamo")
    print("4) Ver libros")
    print("5) Ver usuarios")
    print("6) Ver préstamos")
    print("q) Salir")
    opcion = input("Elige una opción: ").strip().lower()

    if opcion == 'q':
        print("Sistema cerrado. 👋")
        break

    # REGISTRO DE LIBROS
    elif opcion == '1':
        # Pido datos básicos del libro.
        titulo = input("Título del libro: ").strip()
        autor = input("Autor del libro: ").strip()
        id_libro = input("ID único del libro: ").strip()

        # Creo un diccionario y lo agrego a la lista de libros.
        libro = {"titulo": titulo, "autor": autor, "id": id_libro}
        libros.append(libro)
        print("✅ Libro registrado.")

    # REGISTRO DE USUARIOS
    elif opcion == '2':
        nombre = input("Nombre del usuario: ").strip()
        id_usuario = input("ID único del usuario: ").strip()

        usuario = {"nombre": nombre, "id": id_usuario}
        usuarios.append(usuario)
        print("✅ Usuario registrado.")

    # REGISTRO DE PRÉSTAMOS
    elif opcion == '3':
        # Para evitar errores, mostramos los libros y usuarios antes.
        if not libros:
            print("⚠ No hay libros registrados, agrega uno primero.")
            continue
        if not usuarios:
            print("⚠ No hay usuarios registrados, agrega uno primero.")
            continue

        print("\nLibros disponibles:")
        for libro in libros:
            print(f"- {libro['id']} | {libro['titulo']} ({libro['autor']})")

        print("\nUsuarios registrados:")
        for usuario in usuarios:
            print(f"- {usuario['id']} | {usuario['nombre']}")

        id_libro = input("ID del libro a prestar: ").strip()
        id_usuario = input("ID del usuario que lo toma: ").strip()
        fecha = input("Fecha del préstamo (ej: 13/09/2025): ").strip()

        # Creamos el registro del préstamo y lo guardamos.
        prestamo = {"id_libro": id_libro, "id_usuario": id_usuario, "fecha": fecha}
        prestamos.append(prestamo)
        print("✅ Préstamo registrado.")

    # MOSTRAR LIBROS
    elif opcion == '4':
        if not libros:
            print("📭 No hay libros registrados.")
        else:
            print("\n📚 Lista de libros:")
            for libro in libros:
                print(f"ID: {libro['id']} | {libro['titulo']} - {libro['autor']}")

    # MOSTRAR USUARIOS
    elif opcion == '5':
        if not usuarios:
            print("📭 No hay usuarios registrados.")
        else:
            print("\n👥 Lista de usuarios:")
            for usuario in usuarios:
                print(f"ID: {usuario['id']} | {usuario['nombre']}")

    # MOSTRAR PRÉSTAMOS
    elif opcion == '6':
        if not prestamos:
            print("📭 No hay préstamos registrados.")
        else:
            print("\n📖 Lista de préstamos:")
            for p in prestamos:
                print(f"Libro: {p['id_libro']} | Usuario: {p['id_usuario']} | Fecha: {p['fecha']}")

    # Si el usuario pone algo que no existe en el menú.
    else:
        print("Opción no válida. Elige del 1 al 6 o q.")
