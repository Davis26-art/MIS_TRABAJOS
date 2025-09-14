#--------------------------------------------------
# EJERCICIO 29 -- Detectores de palíndromos
#--------------------------------------------------

def es_palindromo_simple(palabra):
    """
    Verifica si una palabra es palíndroma usando un método básico
    Un palíndromo se lee igual de izquierda a derecha y al revés
    """
    palabra_limpia = palabra.lower().replace(" ", "")  # Quitar espacios y minúsculas
    print(f"Verificando si '{palabra}' es un palíndromo:")
    if palabra_limpia == palabra_limpia[::-1]:  # Comparar con la versión invertida
        print(f" ✅ '{palabra}' es un palíndromo")
        return True
    else:
        print(f" ❌ '{palabra}' no es un palíndromo")
        return False


def palindromos_lista(lista_palabras):
    """
    Encuentra todas las palabras palíndromas en una lista
    """
    print(f"\nBuscando palíndromos en la lista: {lista_palabras}")
    palindromos = []
    for palabra in lista_palabras:
        palabra_limpia = palabra.lower().replace(" ", "")
        if palabra_limpia == palabra_limpia[::-1]:
            print(f" 🔎 '{palabra}' es palíndromo")
            palindromos.append(palabra)
        else:
            print(f" → '{palabra}' no es palíndromo")
    return palindromos


def descomponer_en_palindromos(frase):
    """
    Descompone una frase en palabras y muestra cuáles son palíndromos
    """
    print(f"\nAnalizando frase: '{frase}'")
    palabras = frase.split()
    palindromos = []
    for palabra in palabras:
        if palabra.lower() == palabra[::-1].lower():
            print(f" ✨ '{palabra}' es palíndromo dentro de la frase")
            palindromos.append(palabra)
    return palindromos


# Probando detectores de palíndromos
print("ANALIZADOR DE PALÍNDROMOS")
print("=" * 40)

# Verificar palabras individuales
palabras_probar = ["radar", "python", "ana"]
print("1. VERIFICACIÓN INDIVIDUAL:")
for palabra in palabras_probar:
    es_palindromo_simple(palabra)
print()

# Lista de palabras
print("\n2. BÚSQUEDA EN LISTA DE PALABRAS:")
print("-" * 35)
lista = ["oso", "casa", "reconocer", "programa", "salas", "rojo"]
palindromos_en_lista = palindromos_lista(lista)
print(f"\nPalíndromos encontrados: {palindromos_en_lista}")
print(f"Total: {len(palindromos_en_lista)}")

# Descomposición de una frase
print("\n3. DETECCIÓN EN FRASE:")
print("-" * 35)
frase = "ana corre en radar con sus salas"
palindromos_en_frase = descomponer_en_palindromos(frase)
print(f"\nPalíndromos dentro de la frase: {palindromos_en_frase}")
print(f"Total: {len(palindromos_en_frase)}")