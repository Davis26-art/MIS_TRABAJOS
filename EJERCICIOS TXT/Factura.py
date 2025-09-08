# ============================
# FACTURA FRUTERÍA "PEPPEPONGA"
# ============================

# ----------------------------
# Datos iniciales
# ----------------------------
DatosEmisor = ['PeppePonga', 'Cll 17k 16-05', 80541565]  # Info del negocio
DatosReceptor = []  # Aquí se almacenarán los datos del cliente
Frutas = ['Sandía', 'Manzana', 'Fresa', 'Uvas', 'Piña']
PreciosF = [500, 350, 250, 250, 500]
FrutasEscogidas = []
Total = 0

# ----------------------------
# Registro del cliente
# ----------------------------
print("=== Registro de cliente ===")
NombreC = input('Ingresa tu nombre: ')
DireccionC = input('Ingresa tu dirección: ')
TelC = int(input('Ingresa tu teléfono: '))

DatosReceptor.append(NombreC)
DatosReceptor.append(DireccionC)
DatosReceptor.append(TelC)

# ----------------------------
# Bienvenida y catálogo
# ----------------------------
print('\nBienvenido a la frutería favorita de Madrid, bienvenido a PeppePonga')
print('Nuestros productos en paquetes son:\n')
print("Frutas disponibles:", Frutas)
print("Precios:", PreciosF)
print('Ahora dime, ¿qué deseas llevar hoy?\n')

# ----------------------------
# Selección de productos
# ----------------------------
Inicio = "Si"
while Inicio == 'Si':
    Selec = input("Fruta a llevar: ")
    if Selec in Frutas:
        FrutasEscogidas.append(Selec)
    else:
        print("Esa fruta no está disponible, intenta con otra.")

    # Validación de la respuesta del cliente
    Inicio = input("¿Desea llevar algo más? (Si/No): ")
    while Inicio not in ["Si", "No"]:
        print("Respuesta incorrecta, intenta nuevamente.")
        Inicio = input("¿Desea llevar algo más? (Si/No): ")

print("\nTodos tus productos han sido registrados correctamente.\n")

# ----------------------------
# Generación de factura en pantalla
# ----------------------------
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

# Cálculo de impuestos
IVA = Total * 0.19
TotalConIVA = Total + IVA

# Totales
print("\nSUBTOTAL: $" + str(Total))
print("IVA (19%): $" + str(round(IVA, 2)))
print("TOTAL A PAGAR: $" + str(round(TotalConIVA, 2)))

print("\n¡Gracias por comprar en PeppePonga!")

# ----------------------------
# Creación de archivo de factura
# ----------------------------
with open("Factura_PeppePonga.txt", "w", encoding="utf-8") as archivo:
    archivo.write("----------- FACTURA -----------\n\n")

    archivo.write("EMISOR:\n")
    archivo.write("-------------------------------\n")
    archivo.write(f"Nombre: {DatosEmisor[0]}\n")
    archivo.write(f"Dirección: {DatosEmisor[1]}\n")
    archivo.write(f"N° Identificación: {DatosEmisor[2]}\n\n")

    archivo.write("CLIENTE:\n")
    archivo.write("-------------------------------\n")
    archivo.write(f"Nombre: {DatosReceptor[0]}\n")
    archivo.write(f"Dirección: {DatosReceptor[1]}\n")
    archivo.write(f"Teléfono: {DatosReceptor[2]}\n\n")

    archivo.write("PRODUCTOS COMPRADOS:\n")
    archivo.write("-------------------------------\n")
    for fruta in FrutasEscogidas:
        for i in range(len(Frutas)):
            if fruta == Frutas[i]:
                precio = PreciosF[i]
                archivo.write(f"{fruta} - ${precio}\n")

    archivo.write("-------------------------------\n")
    archivo.write(f"\nSUBTOTAL: ${Total}\n")
    archivo.write(f"IVA (19%): ${round(IVA, 2)}\n")
    archivo.write(f"TOTAL A PAGAR: ${round(TotalConIVA, 2)}\n")
    archivo.write("-------------------------------\n")

    archivo.write("\n¡Gracias por comprar en PeppePonga!\n")

print("\nLa factura ha sido guardada en el archivo 'Factura_PeppePonga.txt'")
