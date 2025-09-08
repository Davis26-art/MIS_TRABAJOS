# ============================
# ESCRITURA DE ARCHIVOS EN PYTHON
# ============================

# Se crea (o sobrescribe) el archivo 'Sol.txt'
# encoding='utf-8' asegura compatibilidad con acentos y caracteres especiales.
Archivo = open('Sol.txt', 'w', encoding='utf-8')
Archivo.write('Esta mañana salió el sol por el oriente en una acción maravillosa.')
Archivo.close()  # Siempre es importante cerrar el archivo manualmente

print('Ya se imprimió el archivo Sol.txt.')

# Con 'with open(...)' no es necesario cerrar manualmente,
# ya que se cierra de forma automática al salir del bloque.
with open('Archivo_WithOpen.txt', 'w', encoding='utf-8') as Archivo2:
    Archivo2.write('Este es un ejercicio con with open.')

print('Ya se imprimió el archivo Archivo_WithOpen.txt.')
