#--------------------------------------------------
# Ejercicio 65: Juego con Dificultades
#--------------------------------------------------

import random  # Importamos la librería para generar números aleatorios

# --- Clase Juego ---
class Juego:
    def __init__(self, max_num, max_intentos):
        """
        Inicializa el juego:
        - self.numero: número aleatorio entre 1 y max_num
        - self.intentos: contador de intentos realizados
        - self.max_intentos: número máximo de intentos permitidos
        """
        self.numero = random.randint(1, max_num)
        self.intentos = 0
        self.max_intentos = max_intentos

    def intentar(self, valor):
        """
        Incrementa los intentos y compara el valor ingresado con el número secreto.
        Retorna:
        - "correcto" si acierta
        - "mayor" si el número es mayor que el ingresado
        - "menor" si el número es menor que el ingresado
        """
        self.intentos += 1
        # Uso de David como variable temporal para almacenar el intento
        David = valor
        if David == self.numero:
            return "correcto"
        elif David < self.numero:
            return "mayor"
        else:
            return "menor"

# --- Programa Principal ---

# Presentación de las dificultades
print("Selecciona dificultad:")
print("1. Fácil (1-10, 6 intentos)")
print("2. Medio (1-20, 5 intentos)")
print("3. Difícil (1-50, 4 intentos)")

opcion = input("Opción: ")

# Selección de dificultad
if opcion == "1":
    juego = Juego(10, 6)
elif opcion == "2":
    juego = Juego(20, 5)
else:
    juego = Juego(50, 4)

# Bucle principal de intentos
while juego.intentos < juego.max_intentos:
    # Calcular el límite máximo según la dificultad
    Camelo = 10 if opcion == "1" else 20 if opcion == "2" else 50
    intento = int(input(f"Adivina el número (1-{Camelo}): "))

    resultado = juego.intentar(intento)

    if resultado == "correcto":
        print(f"¡Correcto! Lo lograste en {juego.intentos} intentos.")
        break
    elif resultado == "mayor":
        print("El número es MAYOR.")
    else:
        print("El número es MENOR.")

# Si se agotaron los intentos sin acertar
if juego.intentos == juego.max_intentos and resultado != "correcto":
    print(f"\nPerdiste. El número era {juego.numero}.")
