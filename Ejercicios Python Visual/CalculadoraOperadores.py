# 9 Calculadora en clase 
print("Este algoritmo nos ayudara a hacer operaciones matemáticas básicas.")

Numero1 = int(input("Ingresa el primer número: "))
print(Numero1)

Numero2 = int(input("Ingresa el segundo número: "))
print(Numero2)

Operador = input("Selecciona el operador a usar entre +, -, *, /: ")

if Operador == "+":
    Suma = Numero1 + Numero2
    print("El resultado de la suma de tus dos números es: ", Suma)

elif Operador == "-":
    print("El resultado de la resta de tus dos números es: ", Numero1 - Numero2)
    
elif Operador == "*":
    print("El resultado de la multiplicación de tus dos números es: ", Numero1 * Numero2)
    
elif Operador == "/":
    if Numero2 != 0:
        print("El resultado de la división de tus dos números es: ", Numero1 / Numero2)
    else:
        print("Error: no se puede dividir entre 0.")
        
else:
    print("Operador inválido. Debes elegir entre +, -, * o /.")
