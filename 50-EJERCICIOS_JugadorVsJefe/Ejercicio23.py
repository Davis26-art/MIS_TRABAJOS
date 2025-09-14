#----------------------------------------------
# EJERCICIO 23 -- Funciones con números
#----------------------------------------------

# Función para contar cuántos números hay en la lista
def contar_numeros(lista):
    """Cuenta la cantidad de elementos en una lista de números"""
    return len(lista)

# Función para calcular el número mayor
def numero_mayor(lista):
    """Devuelve el número más grande de la lista"""
    mayor = lista[0]  # Tomamos el primero como referencia
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

# Función para calcular el número menor
def numero_menor(lista):
    """Devuelve el número más pequeño de la lista"""
    menor = lista[0]  # Tomamos el primero como referencia
    for num in lista:
        if num < menor:
            menor = num
    return menor

# Función para calcular el promedio de los números
def promedio(lista):
    """Devuelve el promedio de los números"""
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

# Función para verificar si todos los números son pares
def todos_pares(lista):
    """Verifica si todos los números de la lista son pares"""
    for num in lista:
        if num % 2 != 0:  # Si encuentra un impar, devuelve False
            return False
    return True  # Si no encontró impares, devuelve True


# Probando el analizador de números
numeros = [12, 7, 25, 18, 30, 5, 42]

print("ANALIZADOR DE NÚMEROS")
print(f"Números: {numeros}")
print("-" * 50)
print(f"Cantidad de números: {contar_numeros(numeros)}")
print(f"Número mayor: {numero_mayor(numeros)}")
print(f"Número menor: {numero_menor(numeros)}")
print(f"Promedio: {promedio(numeros):.2f}")
print(f"¿Todos son pares?: {todos_pares(numeros)}")

# Probando con otra lista
lista_pares = [2, 4, 6, 8, 10]
print(f"\nProbando con la lista {lista_pares}")
print(f"¿Todos son pares?: {todos_pares(lista_pares)}")
