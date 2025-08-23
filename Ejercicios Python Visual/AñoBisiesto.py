# 8 Año bisiesto
print("Este algoritmo nos ayudara a saber si un año es bisiesto o no")

Anio = int(input("Ingresa un año: "))

if (Anio % 4 == 0 and Anio % 100 != 0) or (Anio % 400 == 0):
    print("El año es bisiesto")
    
else:
    print("El año NO es bisiesto")