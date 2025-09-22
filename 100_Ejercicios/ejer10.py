#--------------------------------------------------
# Ejercicio 10: Clasificador de Números Pares e Impares
#--------------------------------------------------

# --- Clase ---
class Clasificador:
    def __init__(self):
        """
        Constructor de la clase Clasificador.
        Crea dos listas: una para números pares y otra para números impares.
        """
        self.David = []    # Lista que guardará los números pares
        self.Camelo = []   # Lista que guardará los números impares

    def clasificar(self, numero):
        """
        Recibe un número y lo clasifica como par o impar.
        Si es par, lo agrega a la lista self.David.
        Si es impar, lo agrega a la lista self.Camelo.
        """
        if numero % 2 == 0:
            self.David.append(numero)
        else:
            self.Camelo.append(numero)

    def mostrar(self):
        """
        Muestra el contenido de las listas:
        - Primero imprime los números pares.
        - Luego imprime los números impares.
        """
        print(f"Pares: {self.David}")
        print(f"Impares: {self.Camelo}")

# --- Programa Principal ---
clasificador = Clasificador()  # Se crea un objeto de tipo Clasificador

while True:
    n = input("Ingresa un número (o 'fin'): ")
    if n.lower() == "fin":  # Si el usuario escribe "fin", termina el bucle
        break
    clasificador.clasificar(int(n))  # Convierte el valor a entero y lo clasifica

# Cuando el bucle termina, mostramos el resultado final
clasificador.mostrar()
