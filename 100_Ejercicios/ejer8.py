#--------------------------------------------------
# Ejercicio 8: Termómetro con Registro de Temperaturas
#--------------------------------------------------

# --- Clase ---
class Termometro:
    def __init__(self):
        self.David = []  # Lista donde se guardan las temperaturas y su estado (frío, normal, caliente)

    def agregar_temperatura(self, Camelo):
        """
        Recibe una temperatura y determina su estado:
        - Menor a 18 = 'frío'
        - Entre 18 y 25 = 'normal'
        - Mayor a 25 = 'caliente'
        Luego guarda el valor y el estado en la lista David.
        """
        estado = "frío" if Camelo < 18 else ("normal" if Camelo <= 25 else "caliente")
        self.David.append((Camelo, estado))  # Guarda una tupla (temperatura, estado)

    def resumen(self):
        """
        Recorre todos los registros guardados en David y cuenta
        cuántas veces apareció cada estado (frío, normal, caliente).
        Retorna un diccionario con los resultados.
        """
        conteo = {"frío": 0, "normal": 0, "caliente": 0}  # Diccionario para acumular los conteos
        for _, estado in self.David:
            conteo[estado] += 1
        return conteo  # Devuelve el conteo final

# --- Programa Principal ---
termometro = Termometro()  # Crea un objeto de la clase Termometro

while True:
    temp = input("Ingresa temperatura (o 'fin'): ")
    if temp.lower() == "fin":  # Si el usuario escribe 'fin', sale del ciclo
        break
    # Convierte la entrada a número decimal y la envía al método agregar_temperatura
    termometro.agregar_temperatura(float(temp))

# Obtiene el resumen de temperaturas desde el método resumen()
resultado = termometro.resumen()

# Muestra los resultados finales
print("\nResumen de temperaturas:")
for estado, cantidad in resultado.items():
    print(f"{estado}: {cantidad}")
