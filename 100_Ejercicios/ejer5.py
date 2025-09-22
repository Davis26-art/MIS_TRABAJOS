#--------------------------------------------------
# Ejercicio 5: Juego de Adivinanza
#--------------------------------------------------

import random

# --- Clase ---
class Juego:
    def __init__(self):
        self.David = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10
        self.Camelo = 0  # Contador de intentos

    def intentar(self, valor):
        self.Camelo += 1  # Cada vez que se intenta, suma 1
        if valor == self.David:  # Si el valor coincide con el número secreto
            return True
        return False

# --- Programa Principal ---
juego = Juego()

while True:
    intento = int(input("Adivina el número (1-10): "))
    if juego.intentar(intento):  # Llama al método para verificar si acertó
        print(f"¡Correcto! Lo lograste en {juego.Camelo} intentos.")
        break
    else:
        print("Incorrecto, intenta de nuevo.")
