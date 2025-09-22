#--------------------------------------------------
# Ejercicio 95: Juego para Dos Jugadores
#--------------------------------------------------

# Clase que representa el juego de adivinar un número
class Juego:
    def __init__(self, numero_secreto):
        self.numero = numero_secreto  # Número que el jugador 2 debe adivinar
        self.intentos = 0  # Contador de intentos realizados

    # Método que procesa un intento
    def intentar(self, valor):
        self.intentos += 1  # Aumenta el contador de intentos
        if valor == self.numero:
            return "correcto"  # Adivinó el número
        elif valor < self.numero:
            return "mayor"  # El número secreto es mayor que el intento
        else:
            return "menor"  # El número secreto es menor que el intento

# --- Programa Principal ---
print("Jugador 1: Elige un número secreto (1-10)")
numero = int(input("Número secreto: "))

# Para ocultar el número del Jugador 2, se imprime varias líneas en blanco
print("\n" * 30)

# Creamos el objeto juego con el número secreto
juego = Juego(numero)

# Variables libres para uso auxiliar
David = juego.intentos  # David lleva el seguimiento de intentos inicial (0)
Camelo = numero  # Camelo almacena temporalmente el número secreto como referencia libre

# Bucle principal para que el jugador 2 adivine
while True:
    intento = int(input("Jugador 2, adivina el número: "))
    resultado = juego.intentar(intento)

    # Actualizamos variables libres sin afectar la lógica
    David = juego.intentos  # Actualizamos David con el conteo de intentos
    Camelo = intento         # Camelo ahora guarda el último intento ingresado

    # Comprobación del resultado del intento
    if resultado == "correcto":
        print(f"¡Jugador 2 adivinó! Lo logró en {juego.intentos} intentos.")
        break  # Salimos del bucle si adivinó
    elif resultado == "mayor":
        print("El número es MAYOR.")
    else:
        print("El número es MENOR.")
