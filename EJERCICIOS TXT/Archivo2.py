archivo = open('poc.txt', 'r')
""" archivo.write('Insignia para la clase.') """
contenido = archivo.read()
archivo.close()

print(contenido)

for i in contenido.split():
    print(i)



    