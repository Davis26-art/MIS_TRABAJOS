Archivo = open('Sol.txt', 'w', encoding='utf-8')
Archivo.write('Esta mañana salio el sol por el oriente en una acción maravillosa.')

Archivo.close()
print('Ya se imprimio el Archivo. ')

with open('Archivo_WithOpen.txt', 'w', encoding='utf-8') as Archivo2:
    Archivo2.write('Este es un ejecicio con With Open.')

print('Ya se imprimio el Archivo2. ')


