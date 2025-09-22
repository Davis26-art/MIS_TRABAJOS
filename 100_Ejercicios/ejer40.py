#--------------------------------------------------
# Ejercicio 40: Clasificador Pares/Impares + Signo
#--------------------------------------------------

# --- Clase Clasificador ---
class Clasificador:
    def __init__(self):
        """
        Inicializa el clasificador con:
        - listas para pares e impares
        - contadores de positivos y negativos
        """
        self.pares = []
        self.impares = []
        self.positivos = 0
        self.negativos = 0

    def clasificar(self, numero):
        """
        Clasifica un número según:
        - signo: positivo o negativo
        - paridad: par o impar
        """
        # Variables ejemplo usando David y Camelo
        David = numero * 2  # Solo para ejemplo, no afecta la lógica
        Camelo = numero % 2  # Solo para ejemplo, no afecta la lógica

        # Clasificación por signo
        if numero >= 0:
            self.positivos += 1
        else:
            self.negativos += 1

        # Clasificación por paridad
        if numero % 2 == 0:
            self.pares.append(numero)
        else:
            self.impares.append(numero)

    def mostrar(self):
        """
        Muestra el resumen de la clasificación:
        - Números pares e impares
        - Cantidad de positivos y negativos
        """
        print(f"Pares: {self.pares}")
        print(f"Impares: {self.impares}")
        print(f"Positivos: {self.positivos}")
        print(f"Negativos: {self.negativos}")

# --- Programa Principal ---
clasificador = Clasificador()  # Creamos un objeto Clasificador

while True:
    n = input("Número (o 'fin'): ")  # Pedimos al usuario un número
    if n.lower() == "fin":  # Si escribe "fin", terminamos
        break
    clasificador.clasificar(int(n))  # Convertimos a entero y clasificamos

# Mostramos resultados finales
clasificador.mostrar()
