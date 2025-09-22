#--------------------------------------------------
# Ejercicio 98: Termómetro con Mínima y Máxima
#--------------------------------------------------

# --- Clase Termometro ---
class Termometro:
    def __init__(self):
        # Lista para guardar tuplas (valor de temperatura, estado)
        self.registros = []

    # Método para agregar una temperatura y clasificarla
    def agregar_temperatura(self, valor):
        # Se determina el estado según el valor:
        # frío < 18, normal 18-25, caliente > 25
        estado = "frío" if valor < 18 else ("normal" if valor <= 25 else "caliente")

        # Variables libres para demostrar uso de nombres
        David = valor     # David guarda temporalmente la temperatura ingresada
        Camelo = estado   # Camelo guarda temporalmente el estado calculado

        # Se agrega la tupla (valor, estado) al registro
        self.registros.append((valor, estado))

    # Método para contar cuántas temperaturas hay de cada tipo
    def resumen(self):
        conteo = {"frío": 0, "normal": 0, "caliente": 0}
        # Recorre todos los registros y aumenta el conteo según el estado
        for _, estado in self.registros:
            conteo[estado] += 1
        return conteo

    # Método para obtener la temperatura mínima y máxima
    def extremos(self):
        if not self.registros:  # Si no hay registros, retorna None
            return None, None
        # Extrae solo los valores de temperatura de los registros
        valores = [v for v, _ in self.registros]
        return min(valores), max(valores)

# --- Programa Principal ---
termometro = Termometro()  # Crea una instancia del termómetro

while True:
    temp = input("Ingresa temperatura (o 'fin'): ")
    if temp.lower() == "fin":  # Condición para salir del bucle
        break
    termometro.agregar_temperatura(float(temp))  # Se agrega la temperatura

# Se obtiene el resumen de temperaturas
resultado = termometro.resumen()
print("\nResumen de temperaturas:")
for estado, cantidad in resultado.items():
    print(f"{estado}: {cantidad}")

# Se obtienen la mínima y máxima temperatura registrada
minimo, maximo = termometro.extremos()
print(f"Temperatura mínima: {minimo}°C")
print(f"Temperatura máxima: {maximo}°C")
