#--------------------------------------------------
# Ejercicio 12: Encuesta de Satisfacción
#--------------------------------------------------

# --- Clase ---
class Encuesta:
    def __init__(self):
        """
        Constructor de la clase Encuesta.
        Crea una lista vacía llamada self.David para guardar las respuestas
        como tuplas (nombre, respuesta).
        """
        self.David = []  # Lista de tuplas (nombre, respuesta)

    def agregar_respuesta(self, nombre, Camelo):
        """
        Agrega una respuesta a la lista self.David.
        Cada respuesta se guarda como una tupla: (nombre, Camelo)
        """
        self.David.append((nombre, Camelo))

    def resumen(self):
        """
        Calcula el resumen de la encuesta:
        - Conteo de 'si' y 'no'
        - Porcentaje de satisfacción basado en los 'si'
        """
        conteo = {"si": 0, "no": 0}  # Diccionario para contar respuestas
        for _, resp in self.David:  # Recorre todas las respuestas guardadas
            conteo[resp] += 1
        total = len(self.David)  # Total de respuestas
        porcentaje_si = (conteo["si"] / total) * 100 if total > 0 else 0  # Porcentaje de 'si'
        return conteo, porcentaje_si  # Devuelve el conteo y el porcentaje

# --- Programa Principal ---
encuesta = Encuesta()  # Crea un objeto de la clase Encuesta

while True:
    nombre = input("Nombre (o 'fin'): ")
    if nombre.lower() == "fin":  # Si el usuario escribe "fin", termina el bucle
        break
    Camelo = input("¿Te gustó el producto? (si/no): ").lower()  # Guardamos la respuesta en Camelo
    if Camelo not in ("si", "no"):  # Validación de la respuesta
        print("Respuesta inválida.")
        continue  # Vuelve al inicio del bucle si la respuesta es incorrecta
    encuesta.agregar_respuesta(nombre, Camelo)  # Agrega la respuesta al objeto encuesta

# Obtenemos el resumen de la encuesta
conteo, porcentaje = encuesta.resumen()

# Mostramos los resultados finales
print(f"\nResultados:\nSí: {conteo['si']} - No: {conteo['no']}")
print(f"Porcentaje de satisfacción: {porcentaje:.2f}%")
