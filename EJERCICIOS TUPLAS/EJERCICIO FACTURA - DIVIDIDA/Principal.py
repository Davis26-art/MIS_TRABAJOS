from Tuplas_Listas import DatosEmisor, Frutas, PreciosF
from Ciclos import Seleccionar_Frutas, Calcular_Total, Obtener_Precio
from Diccionarios import Crear_Emisor, Registrar_Cliente

print('\nBienvenido a la frutería favorita de Madrid, bienvenido a PeppePonga')
print('Nuestros productos en paquetes son:')
print(f'Frutas:  {Frutas}')
print(f'Precios: {PreciosF}')
print('Ahora dime que deseas llevar hoy? \n')

Emisor = Crear_Emisor(DatosEmisor[0], DatosEmisor[1], DatosEmisor[2])

Cliente = Registrar_Cliente() 

Escogidas = Seleccionar_Frutas()

print('\n----------- FACTURA ----------- \n')
print('EMISOR: ')
print('Nombre: ', Emisor['Nombre'])
print('Dirección: ', Emisor['Dirección'])
print('NIT: ', Emisor['NIT'])

print('\n----------- CLIENTE ----------- \n')
print('CLIENTE: ')
print('Nombre: ', Cliente['Nombre'])
print('Dirección: ', Cliente['Dirección'])
print('Teléfono: ', Cliente['Teléfono'])

print('\n PRODUCTOS COMPRADOS: ')
for fruta in Escogidas: 
    Precio = Obtener_Precio(fruta)
    print(f'- {fruta} - ${Precio}')


subtotal= Calcular_Total(Escogidas)
iva = subtotal * 0.19 
total = subtotal + iva

print("\nSUBTOTAL: $" + str(subtotal))
print("IVA (19%): $" + str(round(iva, 2)))
print("TOTAL A PAGAR: $" + str(round(total, 2)))

print("\n¡Gracias por comprar en PeppePonga!")
