#--------------------------------------------------
# EJERCICIO 27 -- Comparación de búsquedas (números vs palabras)
#--------------------------------------------------

def busqueda_binaria_palabra(lista, palabra_buscada):
    """
    Implementa búsqueda binaria para encontrar una palabra
    La lista debe estar ordenada alfabéticamente
    """
    izquierda = 0                       # Índice inicial (comienza en la primera posición de la lista)
    derecha = len(lista) - 1            # Índice final (última posición de la lista)
    iteraciones = 0                     # Contador de cuántas veces se repite el ciclo

    print(f"Buscando '{palabra_buscada}' en: {lista}")
    print("\nProceso de búsqueda:")

    # Mientras el rango sea válido (izquierda no sobrepase a derecha)
    while izquierda <= derecha:
        iteraciones += 1
        medio = (izquierda + derecha) // 2   # División entera → posición intermedia de la lista
        palabra_medio = lista[medio]         # Elemento que está en la posición media

        # Mostramos información de la iteración actual
        print(f"\nIteración {iteraciones}:")
        print(f" Rango: posiciones {izquierda} a {derecha}")
        print(f" Medio: posición {medio}, valor '{palabra_medio}'")

        # Caso 1: encontramos la palabra exacta
        if palabra_medio == palabra_buscada:
            print(f" ✅ ¡Encontrado! '{palabra_buscada}' está en posición {medio}")
            return medio

        # Caso 2: la palabra que buscamos está a la "derecha" (alfabéticamente mayor)
        elif palabra_medio < palabra_buscada:
            print(f" 🔎 '{palabra_medio}' < '{palabra_buscada}', buscar en mitad derecha")
            izquierda = medio + 1   # Movemos el límite izquierdo a la derecha del medio

        # Caso 3: la palabra que buscamos está a la "izquierda" (alfabéticamente menor)
        else:
            print(f" 🔎 '{palabra_medio}' > '{palabra_buscada}', buscar en mitad izquierda")
            derecha = medio - 1     # Movemos el límite derecho a la izquierda del medio

    # Si el ciclo termina, significa que no encontramos la palabra
    print(f"\n❌ '{palabra_buscada}' no está en la lista")
    print(f"Total de iteraciones: {iteraciones}")
    return -1

def busqueda_lineal_palabra(lista, palabra_buscada):
    """Búsqueda lineal para comparar eficiencia"""
    comparaciones = 0                     # Contador de comparaciones
    for i in range(len(lista)):           # Recorremos toda la lista elemento por elemento
        comparaciones += 1
        if lista[i] == palabra_buscada:   # Si encontramos la palabra
            return i, comparaciones       # Devolvemos la posición y las comparaciones hechas
    return -1, comparaciones              # Si no se encuentra, devolvemos -1

# Probando las búsquedas
palabras_ordenadas = ["amarillo", "azul", "blanco", "morado", "negro", "rojo", "rosa", "verde"]
buscar = "rojo"

print("COMPARACIÓN DE ALGORITMOS DE BÚSQUEDA (PALABRAS)")
print("=" * 55)
print("Lista ordenada:", palabras_ordenadas)
print(f"Palabra a buscar: '{buscar}'")

# Búsqueda binaria
print("\n1. BÚSQUEDA BINARIA:")
print("-" * 30)
posicion_binaria = busqueda_binaria_palabra(palabras_ordenadas, buscar)

# Búsqueda lineal
print("\n2. BÚSQUEDA LINEAL:")
print("-" * 30)
posicion_lineal, comparaciones_lineales = busqueda_lineal_palabra(palabras_ordenadas, buscar)
print(f"Búsqueda lineal: {comparaciones_lineales} comparaciones")
if posicion_lineal != -1:
    print(f"Elemento encontrado en posición {posicion_lineal}")

print(f"\n📌 Ventaja de búsqueda binaria: Menos comparaciones en listas grandes")
