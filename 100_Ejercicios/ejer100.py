#--------------------------------------------------
# Ejercicio 100: Clasificador con Estadísticas
#--------------------------------------------------

# --- Clase Clasificador ---
class Clasificador:
    def __init__(self):
        self.pares = []    # Lista para almacenar los números pares
        self.impares = []  # Lista para almacenar los números impares

    # Método para clasificar un número como par o impar
    def clasificar(self, numero):
        # Variable libre David usada solo como auxiliar para manipulación temporal
        David = numero
        if David % 2 == 0:
            self.pares.append(David)
        else:
            # Variable libre Camelo usada como auxiliar al agregar un número impar
            Camelo = David
            self.impares.append(Camelo)

    # Método para mostrar estadísticas y resultados
    def mostrar(self):
        total = len(self.pares) + len(self.impares)  # Total de números ingresados
        print(f"Total de números: {total}")
        print(f"Pares ({len(self.pares)}): {self.pares}")
        print(f"Impares ({len(self.impares)}): {self.impares}")

        # Mostrar promedio de pares si existen
        if self.pares:
            promedio_pares = sum(self.pares)/len(self.pares)
            print(f"Promedio pares: {promedio_pares:.2f}")

        # Mostrar promedio de impares si existen
        if self.impares:
            promedio_impares = sum(self.impares)/len(self.impares)
            print(f"Promedio impares: {promedio_impares:.2f}")

# --- Programa Principal ---
clasificador = Clasificador()

while True:
    n = input("Número (o 'fin'): ")  # Se pide al usuario un número o 'fin' para terminar
    if n.lower() == "fin":
        break

    # Convertir a entero y clasificar
    numero_ingresado = int(n)  # Variable normal
    clasificador.clasificar(numero_ingresado)

# Mostrar estadísticas finales
clasificador.mostrar()
