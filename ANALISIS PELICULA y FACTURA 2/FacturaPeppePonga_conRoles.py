DatosEmisor = ['PeppePonga', 'cll 17k 16-05', 80541565]
DatosReceptor = []
Frutas = ['Sandia', 'Manzana', 'Fresa', 'Uvas', 'Piña']
PreciosF = [500, 350, 250, 250, 500]

# --- MENÚ PRINCIPAL ---
opcion_principal = ""
while opcion_principal != "3":
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Modo Empleado")
    print("2. Modo Cliente")
    print("3. Salir")
    opcion_principal = input("Seleccione una opción: ")

    # --- MODO EMPLEADO ---
    if opcion_principal == "1":
        opcion = ""
        while opcion != "4":
            print("\n--- MENÚ EMPLEADO ---")
            print("1. Agregar fruta")
            print("2. Actualizar precio de fruta")
            print("3. Eliminar fruta")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":  # Esta opcion es para agregar una fruta nueva
                nueva_fruta = input("Ingrese el nombre de la nueva fruta: ")
                nuevo_precio = int(input("Ingrese el precio de esa fruta: "))
                Frutas.append(nueva_fruta)
                PreciosF.append(nuevo_precio)
                print(f"\nFruta '{nueva_fruta}' agregada con precio ${nuevo_precio}.")

            elif opcion == "2": # Esta opcion es para actualizar el precio de un fruta existente
                fruta_modi = input("Ingrese el nombre de la fruta a actualizar: ")
                if fruta_modi in Frutas:
                    pos = Frutas.index(fruta_modi)
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    PreciosF[pos] = nuevo_precio
                    print(f"\nPrecio de '{fruta_modi}' actualizado a ${nuevo_precio}.")
                else:
                    print("Esa fruta no existe.")

            elif opcion == "3":   # Esta opcion es para eliminar una fruta y su precio dentro de las listas
                borrar_fruta = input("Ingrese el nombre de la fruta a eliminar: ")
                if borrar_fruta in Frutas:
                    pos = Frutas.index(borrar_fruta)
                    Frutas.pop(pos)
                    PreciosF.pop(pos)
                    print(f"\nFruta '{borrar_fruta}' eliminada correctamente.")
                else:
                    print("Esa fruta no existe.")

            elif opcion == "4": # Esta opcion es para salir de este menú
                print("Volviendo al menú principal...")
            else:
                print("Opción inválida.")

    # --- MODO CLIENTE ---
    elif opcion_principal == "2":
        DatosReceptor.clear()   # Esto nos ayuda a limpiar los datos de clientes anteriores si no salimos del programa y queremos hacer el proceso como cliente de nuevo.
        FrutasEscogidas = []
        Total = 0
        Inicio = "Si"

        NombreC = input('Ingresa tu nombre: ')
        DireccionC = input('Ingresa tu dirección: ')
        TelC = int(input('Ingresa tu telefóno: '))

        DatosReceptor.append(NombreC)
        DatosReceptor.append(DireccionC)
        DatosReceptor.append(TelC)

        print('\nBienvenido a la frutería favorita de Madrid, bienvenido a PeppePonga')
        print('Nuestros productos en paquetes son:')
        print('Frutas:')
        print(Frutas)
        print('Precios:')
        print(PreciosF)
        print('Ahora dime, ¿qué deseas llevar hoy?\n')

        while Inicio == 'Si':
            Selec = input("Fruta a llevar: ")
            if Selec in Frutas:
                FrutasEscogidas.append(Selec)
            else:
                print("Esa fruta no está disponible, intenta con otra.")
            Inicio = input("¿Desea llevar algo más? (Si/No): ")
            while Inicio not in ["Si", "No"]:
                print("Respuesta incorrecta, intenta nuevamente.")
                Inicio = input("¿Desea llevar algo más? (Si/No): ")

        print("\nTodos tus productos han sido registrados correctamente.\n")

        print("----- FACTURA -----\n")
        print("EMISOR:")
        print("Nombre:", DatosEmisor[0])
        print("Dirección:", DatosEmisor[1])
        print("N° Identificación:", DatosEmisor[2])

        print("\nCLIENTE:")
        print("Nombre:", DatosReceptor[0])
        print("Dirección:", DatosReceptor[1])
        print("Teléfono:", DatosReceptor[2])

        print("\nPRODUCTOS COMPRADOS:")
        for fruta in FrutasEscogidas:
            for i in range(len(Frutas)):
                if fruta == Frutas[i]:
                    precio = PreciosF[i]
                    print(f"{fruta} - ${precio}")
                    Total += precio

        IVA = Total * 0.19
        TotalConIVA = Total + IVA

        print("\nSUBTOTAL: $" + str(Total))
        print("IVA (19%): $" + str(round(IVA, 2)))
        print("TOTAL A PAGAR: $" + str(round(TotalConIVA, 2)))

        print("\n¡Gracias por comprar en PeppePonga!")

    elif opcion_principal == "3":
        print("\nCerrando sistema...")
    else:
        print("Opción inválida, intente nuevamente.")




