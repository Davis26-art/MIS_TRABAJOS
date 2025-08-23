# 6 Número positivo o negativo
print("Este algoritmo nos ayudara a saber si un número es positivo, negativo o cero")

Numero = int(input("Ingresa un número: "))

if Numero > 0:
    print("El número ", Numero, " es positivo")
    
elif Numero < 0:
    print("El número ", Numero, " es negativo")
    
else:
    print("El número es cero")