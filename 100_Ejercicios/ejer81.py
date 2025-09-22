#--------------------------------------------------
# Ejercicio 81: Encuesta con Respuestas en Mayúsculas
#--------------------------------------------------

# --- Clase Encuesta ---
class Encuesta:
    def __init__(self):
        """
        Inicializa la encuesta con una lista vacía de respuestas.
        Cada respuesta será una tupla (nombre, respuesta_en_mayúsculas)
        """
        self.respuestas = []

    def agregar_respuesta(self, nombre, respuesta):
        """
        Agrega una respuesta a la lista.
        Convierte la respuesta a mayúsculas para uniformidad.
        """
        self.respuestas.append((nombre, respuesta.upper()))

    def mostrar_resultados(self):
        """
        Cuenta cuántas respuestas son 'SÍ' y cuántas 'NO'.
        Retorna un diccionario con los totales.
        """
        conteo = {"SÍ": 0, "NO": 0}
        for _, r in self.respuestas:
            if r in conteo:
                conteo[r] += 1
        return conteo

# --- Programa Principal ---
encuesta = Encuesta()  # Creamos instancia de la encuesta
resultados = {}        # Diccionario auxiliar para guardar respuestas por persona

while True:
    nombre = input("Nombre (o 'fin'): ")  # Pedimos el nombre del participante
    if nombre.lower() == "fin":           # Condición de salida
        break

    respuesta = input("¿Te gustó el servicio? (sí/no): ").upper()  # Pregunta de la encuesta
    if respuesta not in ("SÍ", "NO"):    # Validación de respuesta
        print("Respuesta inválida.")
        continue

    # Agregamos la respuesta a la encuesta
    encuesta.agregar_respuesta(nombre, respuesta)
    resultados[nombre] = respuesta

    # Variables auxiliares solicitadas
    David = len(nombre)     # Cantidad de letras en el nombre ingresado
    Camelo = respuesta      # Guardamos la respuesta del usuario (puede usarse para alertas o análisis)

# --- Mostrar Resultados ---
print("\nResultados individuales:")
for persona, r in resultados.items():
    print(f"{persona}: {r}")

# --- Resumen total ---
conteo = encuesta.mostrar_resultados()
print(f"\nTotal SÍ: {conteo['SÍ']}, Total NO: {conteo['NO']}")
