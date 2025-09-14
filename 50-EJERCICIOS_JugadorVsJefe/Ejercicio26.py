#----------------------------------------------
# EJERCICIO 26 -- Algoritmo de búsqueda lineal
#----------------------------------------------

def busqueda_lineal(lista, objetivo):
    """
    Implementa el algoritmo de búsqueda lineal.
    Recorre la lista elemento por elemento hasta encontrar el objetivo.
    """
    comparaciones = 0  # Contador de comparaciones realizadas
    print(f"Lista: {lista}")
    print(f"Buscando el número: {objetivo}")
    print("\nProceso paso a paso:")

    # Recorrer la lista
    for i in range(len(lista)):
        comparaciones += 1
        print(f"Comparación {comparaciones}: ¿{lista[i]} == {objetivo}?")

        if lista[i] == objetivo:  # Si encontramos el número
            print(f"✔ Elemento encontrado en la posición {i}")
            print(f"\nTotal de comparaciones: {comparaciones}")
            return i

        else:
            print("✘ No es el elemento buscado")

    # Si llegamos aquí, el número no estaba en la lista
    print("\n❌ Elemento no encontrado en la lista")
    print(f"Total de comparaciones: {comparaciones}")
    return -1


# Probando el algoritmo de búsqueda lineal
numeros = [15, 8, 42, 23, 4, 16, 9]
print("ALGORITMO DE BÚSQUEDA LINEAL")
print("=" * 45)

# Caso 1: número existente
pos = busqueda_lineal(numeros, 23)

# Caso 2: número que no existe
pos = busqueda_lineal(numeros, 50)
