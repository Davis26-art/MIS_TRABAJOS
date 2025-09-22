#--------------------------------------------------
# Ejercicio 14: Clasificador de Palabras
#--------------------------------------------------

# --- Clase ---
class ClasificadorPalabras:
    def __init__(self):
        """
        Constructor de la clase ClasificadorPalabras.
        Crea una lista vacía llamada self.David para guardar las palabras
        junto con su tipo ("corta" o "larga").
        """
        self.David = []  # Lista de tuplas (palabra, tipo)

    def agregar_palabra(self, Camelo):
        """
        Clasifica la palabra Camelo como 'corta' o 'larga' y la agrega a la lista.
        - 'corta' si tiene 4 o menos caracteres
        - 'larga' si tiene más de 4 caracteres
        """
        tipo = "corta" if len(Camelo) <= 4 else "larga"
        self.David.append((Camelo, tipo))

    def mostrar(self):
        """
        Muestra todas las palabras y su clasificación.
        """
        for palabra, tipo in self.David:
            print(f"{palabra} es {tipo}")

# --- Programa Principal ---
clasificador = ClasificadorPalabras()  # Creamos un objeto de la clase
diccionario = {}  # Diccionario palabra: tipo para acceso rápido

while True:
    David = input("Ingresa una palabra (o 'fin'): ")  # Variable David guarda la palabra ingresada
    if David.lower() == "fin":  # Termina el bucle si escribe "fin"
        break
    clasificador.agregar_palabra(David)  # Agrega la palabra al objeto clasificador
    # También la agregamos al diccionario con su tipo
    diccionario[David] = "corta" if len(David) <= 4 else "larga"

# Mostramos todas las palabras clasificadas
clasificador.mostrar()
