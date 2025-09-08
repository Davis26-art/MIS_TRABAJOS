# ============================
# MANEJO DE ARCHIVOS EN PYTHON
# ============================

# Apertura de un archivo existente en modo lectura
# 'r' significa "read" (solo lectura).
archivo1 = open('dac.txt', 'r')
contenido = archivo1.read()   # Se lee todo el contenido del archivo
archivo1.close()              # Siempre se cierra el archivo después de usarlo

# Se imprime en pantalla el contenido leído
print(f'Documento leído: {contenido}')


# ==============================
# CREACIÓN Y ESCRITURA DE ARCHIVOS
# ==============================

# Nota: El código siguiente estaba comentado en tu versión.
# Lo organizo y explico aquí, pero puedes descomentar si lo quieres usar.

# Abrir archivo en modo escritura 'w'
# Si el archivo no existe, se crea. Si existe, se sobrescribe.
"""
archivo2 = open('dec.txt', 'w')
archivo2.write('Hoy ordena el archivo en b')
archivo2.close()
print('Documento dec.txt creado e impreso.')

archivo3 = open('dic.txt', 'w')
archivo3.write('Hoy ordena el archivo en c')
archivo3.close()
print('Documento dic.txt creado e impreso.')

archivo4 = open('doc.txt', 'w')
archivo4.write('Hoy ordena el archivo en d')
archivo4.close()
print('Documento doc.txt creado e impreso.')

archivo5 = open('duc.txt', 'w')
archivo5.write('Hoy ordena el archivo en e')
archivo5.close()
print('Documento duc.txt creado e impreso.')
"""


# =======================================
# CREACIÓN DE VARIOS ARCHIVOS CON UN BUCLE
# =======================================

# Otra forma más eficiente sería usar un ciclo for
# para no repetir tanto código.
"""
for i, letra in enumerate(['b', 'c', 'd', 'e'], start=2):
    nombre_archivo = f'archivo{i}.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f'Hoy ordena el archivo en {letra}')
    print(f'Documento {nombre_archivo} creado e impreso.')
"""
