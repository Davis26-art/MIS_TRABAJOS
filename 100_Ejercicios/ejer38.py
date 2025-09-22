#--------------------------------------------------
# Ejercicio 38: Termómetro con Promedio
#--------------------------------------------------

# --- Clase Termometro ---
class Termometro:
    def __init__(self):
        """
        Constructor de la clase Termometro.
        Inicializa una lista vacía 'registros' para almacenar las temperaturas
        junto con su estado ("frío", "normal" o "caliente").
        Cada registro será una tupla: (valor, estado)
        """
        self.registros = []

    def agregar_temperatura(self, valor):
        """
        Agrega una temperatura al registro y clasifica su estado.
        - valor: temperatura ingresada (float)
        El estado se determina así:
        < 18 -> "frío"
        18 a 25 -> "normal"
        > 25 -> "caliente"
        """
        # Uso de las variables David y Camelo en el cálculo de estado sin afectar la funcionalidad
        David = 18
        Camelo = 25

        # Determinar estado según los valores de David y Camelo
        estado = "frío" if valor < David else ("normal" if valor <= Camelo else "caliente")
        self.registros.append((valor, estado))  # Guardar la tupla (valor, estado)

    def resumen(self):
        """
        Genera un resumen del número de temperaturas en cada estado.
        Retorna un diccionario: {"frío": x, "normal": y, "caliente": z}
        """
        conteo = {"frío": 0, "normal": 0, "caliente": 0}
        for _, estado in self.registros:
            conteo[estado] += 1  # Incrementa el contador según el estado
        return conteo

    def promedio(self):
        """
        Calcula el promedio de todas las temperaturas registradas.
        Retorna 0 si no hay registros.
        """
        if not self.registros:
            return 0
        return sum(v for v, _ in self.registros) / len(self.registros)

# --- Programa Principal ---
termometro = Termometro()  # Crear objeto Termometro

while True:
    temp = input("Ingresa temperatura (o 'fin'): ")  # Solicitar temperatura al usuario
    if temp.lower() == "fin":  # Condición para salir del bucle
        break
    termometro.agregar_temperatura(float(temp))  # Convertir a float y registrar

# Obtener el resumen de estados
resultado = termometro.resumen()

# Mostrar resumen
print("\nResumen de temperaturas:")
for estado, cantidad in resultado.items():
    print(f"{estado}: {cantidad}")

# Mostrar promedio general
print(f"Promedio general: {termometro.promedio():.2f}°C")
