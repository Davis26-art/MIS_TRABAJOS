Datos_Receptor = {}

def Crear_Emisor(Nombre, Direccion, NIT):
    
    return {
        'Nombre': Nombre,
        'Dirección': Direccion,
        'NIT': NIT
    }
    
def Registrar_Cliente():
    Nombre = input('Ingresa tu nombre: ')
    Direccion = input('Ingresa tu dirección: ')
    Telefono = int(input('Ingresa tu teléfono: '))

    return {
        'Nombre': Nombre,
        'Dirección': Direccion,
        'Teléfono': Telefono
    }   