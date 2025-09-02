from Tuplas_Listas import Frutas, PreciosF

def Seleccionar_Frutas():
    Frutas_Selec = []
    Inicio = 'Si'
    
    while Inicio == 'Si':
        Fruta = input('Fruta a llevar: ')
        if Fruta in Frutas:
            Frutas_Selec.append(Fruta)
        
        else:
            print('Esta fruta no está disponible, intenta con otra.')
            
        Inicio = input('¿Desea llevar algo más? (Si/No)')
        
        while Inicio not in ['Si', 'No']:
            print('Esta respuesta es incorrecta, intenta nuevamente.')
            Inicio = input('¿Desea llevar algo más? (Si/No)')
            
    return Frutas_Selec


def Calcular_Total(Frutas_Selec):
    Total = 0
    for fruta in Frutas_Selec:
        for i in range(len(Frutas)):
            if fruta == Frutas[i]: 
                Total += PreciosF[i]
        
    return Total


def Obtener_Precio(fruta):
    for i in range(len(Frutas)):
        if fruta == Frutas[i]:
            return PreciosF[i]
    return 0 