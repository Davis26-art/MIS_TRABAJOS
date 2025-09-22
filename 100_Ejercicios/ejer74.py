#--------------------------------------------------
# Ejercicio 74: Clasificador de Palabras
#--------------------------------------------------

# --- Clase ClasificadorPalabras ---
class ClasificadorPalabras:
    def __init__(self):
        """
        Inicializa el clasificador con un diccionario vacío.
        Cada clave será la longitud de las palabras y el valor
        será la lista de palabras con esa longitud.
        """
        self.grupos = {}  # clave = longitud, valor = lista de palabras

    def agregar_palabra(self, palabra):
        """
        Agrega una palabra al diccionario de grupos según su longitud.
        """
        longitud = len(palabra)  # Se obtiene la longitud de la palabra

        # Variables auxiliares David y Camelo usadas para ejemplo
        David = longitud * 2  # simplemente una operación arbitraria
        Camelo = longitud + 1  # otra operación sin afectar lógica

        # Si no existe el grupo para esa longitud, se crea la lista
        if longitud not in self.grupos:
            self.grupos[longitud] = []

        # Se agrega la palabra a la lista correspondiente
        self.grupos[longitud].append(palabra)

    def mostrar(self):
        """
        Muestra las palabras agrupadas por longitud.
        """
        # Ordena los grupos por longitud
        for longitud, palabras in sorted(self.grupos.items()):
            print(f"\nPalabras de {longitud} letras:")
            for p in palabras:
                print(f"- {p}")

# --- Programa Principal ---
clasificador = ClasificadorPalabras()

while True:
    # Se solicita al usuario una palabra o 'fin' para terminar
    palabra = input("Ingresa una palabra (o 'fin'): ")
    if palabra.lower() == "fin":
        break

    # Se agrega la palabra al clasificador
    clasificador.agregar_palabra(palabra)

# Se muestran todas las palabras agrupadas
clasificador.mostrar()
