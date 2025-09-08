Personaje = {'Nombre: ': '',
             'Vida: ': 7,
             'Velocidad: ': '',
             'Daño: ': '', 
             'Clase: ': '',
             'Arma: ': '',
             'Habilidad: ': '',
             'Armadura': ''
             }

nombre = input('Ingresa un nombre para el personaje: ')
#Vida = 7
Velocidad = ('Normal', 'Rápido', 'Superior')
Daño = ('Bajo', 'Medio', 'Alto')
Clases = ('Guerrero', 'Mago', 'Arquero')
Armas = ['Espada', 'Bastón', 'Arco']
Habilidades = ['Fuerza', 'Magia', 'Agilidad']
Armadura = ['Ligera', 'Mediana', 'Pesada']

Personaje['Nombre: '] = nombre

print('\n Elige la velocidad de tu personaje: ')
for i, velo in enumerate(Velocidad, 1):
    print(i, velo)
    
opcion = int(input('Selecciona la opción de tu velocidad: '))
Personaje['Velocidad: '] = Velocidad[opcion - 1]


print('\n Elige el daño de tu personaje: ')
for i, dano in enumerate(Daño, 1):
    print(i, dano)

opcion = int(input('Selecciona la opción de tu daño: '))
Personaje['Daño: '] = Daño[opcion - 1]


print('\n Elige la clase de tu personaje: ')
for i, clase in enumerate(Clases, 1):
    print(i, clase)

opcion = int(input('Selecciona la opción de tu clase: '))
Personaje['Clase: '] = Clases[opcion - 1]
    
    
print('\n Elige el arma de tu personaje: ')
for i, arma in enumerate(Armas, 1):
    print(i, arma)
    
opcion = int(input('Selecciona la opción de tu arma: '))
Personaje['Arma: '] = Armas[opcion - 1]


print('\n Elige la habilidad de tu personaje: ')
for i, habili in enumerate(Habilidades, 1):
    print(i, habili)
    
opcion = int(input('Selecciona la opción de tu habilidad: '))
Personaje['Habilidad: '] = Habilidades[opcion - 1]


print('\n Elige la armadura de tu personaje: ')
for i, armad in enumerate(Armadura, 1):
    print(i, armad)
    
opcion = int(input('Selecciona la opción de tu armadura: '))
Personaje['Armadura'] = Armadura[opcion - 1]
    
    
print('\n Personaje creado: ')
for clave, valor in Personaje.items():
    print(f'{clave}: {valor}')
     
    
while True:
    opcion = input('\n ¿Desea relizar algún cambio en su personaje? (Si/No): ')
    if opcion == 'No':
        break
    
    elif opcion == 'Si':
        print('\n ¿Qué deseas modificar? ')
        print('1. Nombre \n2. Velocidad \n3. Daño \n4. Clase \n5. Arma \n6. Habilidad \n7. Armadura')
        eleccion = int(input('Selecciona el atrubuto a modificar: '))
        
        if eleccion == 1:
            Personaje['Nombre: '] = input('Nuevo nombre: ')
            
        elif eleccion == 2: 
            for i, velo in enumerate(Velocidad, 1):
                print(i, velo)
                
            opcion = int(input('Selecciona la nueva velocidad de tu personaje: '))
            Personaje['Velocidad: '] = Velocidad[opcion - 1]
            
        elif eleccion == 3: 
            for i, dano in enumerate(Daño, 1):
                print(i, dano)
                
            opcion = int(input('Selecciona el nuevo daño de tu personaje: '))
            Personaje['Daño: '] = Daño[opcion - 1]
            
        elif eleccion == 4:
            for i, clase in enumerate(Clases, 1):
                print(i, clase)
                
            opcion = int(input('\n Selecciona la nueva clase del personaje: '))
            Personaje['Clase: '] = Clases[opcion - 1]
            
        elif eleccion == 5: 
            for i, arma in enumerate(Armas, 1):
                print(i, arma)
                
            opcion = int(input('\n Selecciona la nueva arma del personaje: '))
            Personaje['Arma: '] = Armas[opcion - 1]
            
        elif eleccion == 6: 
            for i, habili in enumerate(Habilidades, 1):
                print(i, habili)
                
            opcion = int(input('\n Selecciona la nueva arma del personaje: '))
            Personaje['Habilidad: '] = Habilidades[opcion - 1]
            
        elif eleccion == 7: 
            for i, armad in enumerate(Armadura, 1):
                print(i, armad)
                
            opcion = int(input('Selecciona la nueva armadura de tu personaje: '))
            Personaje['Armadura'] = Armadura[opcion - 1]
            
        else:
            print('Elección no valida, intenta nuevamente.  ')
            
    else:
        print('Responde con "Si" o "No" ')
        
print('\n Personaje finalizado con Exitó: ')
for clave, valor in Personaje.items():
    print(f'{clave}: {valor}')

     
     
     
