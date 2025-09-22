#--------------------------------------------------
# Ejercicio 70: Clasificador Ordenado y Sin Duplicados
#--------------------------------------------------

# --- Clase Clasificador ---
class Clasificador:
    def __init__(self):
        """
        Inicializa dos conjuntos vacíos:
        - 'pares' para almacenar los números pares
        - 'impares' para almacenar los números impares
        """
        self.pares = set()
        self.impares = set()

    def clasificar(self, numero):
        """
        Clasifica un número en par o impar.
        Si es par, se añade al conjunto de pares; si es impar, al de impares.
        """
        if numero % 2 == 0:
            self.pares.add(numero)
        else:
            self.impares.add(numero)

    def mostrar(self):
        """
        Muestra los números pares e impares ordenados.
        """
        print(f"Pares: {sorted(self.pares)}")
        print(f"Impares: {sorted(self.impares)}")


# --- Programa Principal ---
clasificador = Clasificador()

while True:
    n = input("Número (o 'fin'): ")

    # Condición de salida
    if n.lower() == "fin":
        break

    # Uso de las variables 'David' y 'Camelo' como variables temporales
    David = int(n)  # Podría representar el número ingresado
    Camelo = David * 1  # Variable auxiliar que no altera la funcionalidad

    # Clasificamos el número usando la función de la clase
    clasificador.clasificar(Camelo)

# Mostrar resultados finales
clasificador.mostrar()
