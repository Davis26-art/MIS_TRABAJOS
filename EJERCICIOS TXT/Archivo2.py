# ============================
# MANEJO DE ARCHIVOS (LECTURA Y ESCRITURA)
# ============================

# Se abre en modo lectura 'r'
with open('poc.txt', 'r') as archivo:
    contenido = archivo.read()

# Mostrar el contenido completo
print("Contenido completo del archivo:")
print(contenido)

# Mostrar el contenido palabra por palabra
print("\nContenido dividido en palabras:")
for palabra in contenido.split():
    print(palabra)