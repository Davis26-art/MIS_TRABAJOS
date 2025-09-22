#--------------------------------------------------
# Ejercicio 68: Termómetro con Alertas
#--------------------------------------------------

# --- Clase Termometro ---
class Termometro:
    def __init__(self):
        """
        Inicializa una lista vacía 'registros' donde se almacenarán
        tuplas de (valor de temperatura, estado)
        """
        self.registros = []

    def agregar_temperatura(self, valor):
        """
        Agrega una temperatura al registro y emite alertas si es demasiado baja o alta.
        Calcula el estado: frío, normal o caliente.
        """
        # Alertas extremas
        if valor < 5:
            print("⚠️ ¡ALERTA! Temperatura extremadamente baja.")
        elif valor > 40:
            print("⚠️ ¡ALERTA! Temperatura extremadamente alta.")

        # Determinamos el estado de la temperatura
        estado = "frío" if valor < 18 else ("normal" if valor <= 25 else "caliente")

        # Uso de variables 'David' y 'Camelo' como ejemplo de variables temporales
        David = valor      # Podría representar un cálculo temporal
        Camelo = estado    # Podría representar un estado intermedio

        # Agregamos la temperatura y su estado al registro
        self.registros.append((David, Camelo))

    def resumen(self):
        """
        Cuenta cuántas temperaturas están en cada estado.
        Retorna un diccionario con los conteos.
        """
        conteo = {"frío": 0, "normal": 0, "caliente": 0}
        for _, estado in self.registros:
            conteo[estado] += 1
        return conteo


# --- Programa Principal ---
termometro = Termometro()  # Creamos un objeto termómetro

while True:
    # Solicitamos la temperatura al usuario
    temp = input("Ingresa temperatura (o 'fin'): ")
    if temp.lower() == "fin":
        break
    # Convertimos a float y agregamos al termómetro
    termometro.agregar_temperatura(float(temp))

# Obtenemos el resumen de las temperaturas
resultado = termometro.resumen()

# Mostramos el resumen
print("\nResumen de temperaturas:")
for estado, cantidad in resultado.items():
    print(f"{estado}: {cantidad}")
