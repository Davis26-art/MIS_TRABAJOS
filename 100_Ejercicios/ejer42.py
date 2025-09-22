#--------------------------------------------------
# Ejercicio 42: Encuesta con opción "regular"
#--------------------------------------------------

# --- Clase Encuesta ---
class Encuesta:
    def __init__(self):
        """
        Inicializa la lista de respuestas.
        Cada respuesta se guarda como tupla: (nombre, respuesta)
        """
        self.respuestas = []

    def agregar_respuesta(self, nombre, respuesta):
        """
        Agrega una respuesta a la lista
        nombre: nombre del encuestado
        respuesta: 'si', 'no' o 'regular'
        """
        self.respuestas.append((nombre, respuesta))

    def resumen(self):
        """
        Genera un resumen de la encuesta:
        - Conteo de cada tipo de respuesta
        - Porcentaje de 'si' sobre el total
        """
        conteo = {"si": 0, "no": 0, "regular": 0}
        for _, resp in self.respuestas:
            conteo[resp] += 1

        total = len(self.respuestas)
        porcentaje_si = (conteo["si"] / total) * 100 if total > 0 else 0

        # Variables de ejemplo usando David y Camelo sin afectar la funcionalidad
        David = conteo["si"]  # Guarda número de respuestas 'si'
        Camelo = conteo["regular"]  # Guarda número de respuestas 'regular'

        return conteo, porcentaje_si

# --- Programa Principal ---
encuesta = Encuesta()

while True:
    nombre = input("Nombre (o 'fin'): ")
    if nombre.lower() == "fin":  # Condición de salida
        break

    # Preguntar por la respuesta
    respuesta = input("¿Te gustó el producto? (si/no/regular): ").lower()

    # Validación de respuesta
    if respuesta not in ("si", "no", "regular"):
        print("Respuesta inválida.")
        continue

    # Agregar respuesta al objeto encuesta
    encuesta.agregar_respuesta(nombre, respuesta)

# Obtener resumen de la encuesta
conteo, porcentaje = encuesta.resumen()

# Mostrar resultados
print(f"\nResultados:")
print(f"Sí: {conteo['si']} - No: {conteo['no']} - Regular: {conteo['regular']}")
print(f"Porcentaje de satisfacción (Sí): {porcentaje:.2f}%")
