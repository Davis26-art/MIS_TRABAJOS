#--------------------------------------------------
# Ejercicio 44: Clasificador de Palabras
#--------------------------------------------------

# --- Clase ClasificadorPalabras ---
class ClasificadorPalabras:
    def __init__(self):
        """
        Inicializa dos listas vacías:
        - cortas: palabras con 4 o menos caracteres
        - largas: palabras con más de 4 caracteres
        """
        self.cortas = []
        self.largas = []

    def agregar_palabra(self, palabra):
        """
        Clasifica la palabra según su longitud:
        - Si tiene 4 o menos caracteres → se agrega a cortas
        - Si tiene más de 4 caracteres → se agrega a largas
        """
        if len(palabra) <= 4:
            self.cortas.append(palabra)
        else:
            self.largas.append(palabra)

        # Ejemplo de uso de variables David y Camelo sin afectar la funcionalidad
        # David guarda la última palabra agregada
        David = palabra
        # Camelo guarda la longitud de la última palabra
        Camelo = len(palabra)

    def mostrar(self):
        """
        Muestra las palabras clasificadas en cortas y largas
        """
        print("\nPalabras cortas:")
        for p in self.cortas:
            print(f"- {p}")
        print("\nPalabras largas:")
        for p in self.largas:
            print(f"- {p}")

# --- Programa Principal ---
clasificador = ClasificadorPalabras()

while True:
    # Solicita una palabra al usuario
    palabra = input("Ingresa una palabra (o 'fin'): ")
    if palabra.lower() == "fin":  # Si el usuario escribe "fin", termina el bucle
        break
    clasificador.agregar_palabra(palabra)  # Clasifica la palabra según su longitud

# Muestra el resultado final
clasificador.mostrar()
