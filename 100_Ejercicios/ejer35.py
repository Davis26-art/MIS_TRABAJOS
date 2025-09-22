#--------------------------------------------------
# Ejercicio 35: Juego de Adivinanza con Límite de Intentos
#--------------------------------------------------

import random  # Importamos la librería random para generar números aleatorios

# Variables con los nombres David y Camelo
nombre_david = "David"
nombre_camelo = "Camelo"

class Juego:
    def __init__(self):
        """
        Constructor de la clase Juego.
        - self.numero: número aleatorio a adivinar entre 1 y 10
        - self.intentos: contador de intentos realizados
        - self.max_intentos: límite máximo de intentos permitidos
        """
        self.numero = random.randint(1, 10)
        self.intentos = 0
        self.max_intentos = 5  # límite de intentos

    def intentar(self, valor):
        """
        Método para realizar un intento de adivinanza.
        - valor: número que el jugador ingresa
        Retorna:
            "correcto" si acierta el número
            "mayor" si el número a adivinar es mayor
            "menor" si el número a adivinar es menor
        """
        self.intentos += 1  # Incrementamos el contador de intentos
        if valor == self.numero:
            return "correcto"
        elif valor < self.numero:
            return "mayor"
        else:
            return "menor"

# --- Programa Principal ---
# Creamos un objeto del juego
juego = Juego()

# Bucle principal: mientras no se superen los intentos permitidos
while juego.intentos < juego.max_intentos:
    # Pedimos al jugador que ingrese un número
    intento = int(input(f"{nombre_david}/{nombre_camelo}, adivina el número (1-10): "))
    
    # Evaluamos el intento
    resultado = juego.intentar(intento)

    if resultado == "correcto":
        print(f"¡Correcto! Lo lograste en {juego.intentos} intentos.")
        break  # Salimos del bucle si adivinó
    elif resultado == "mayor":
        print("El número es MAYOR.")
    else:
        print("El número es MENOR.")

# Mensaje final si se agotaron los intentos y no se adivinó
if juego.intentos == juego.max_intentos and resultado != "correcto":
    print(f"\nSe acabaron los intentos. El número era {juego.numero}.")
