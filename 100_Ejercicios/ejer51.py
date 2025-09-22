#--------------------------------------------------
# Ejercicio 51: Encuesta con Porcentaje de Satisfacción
#--------------------------------------------------

# --- Clase Encuesta ---
class Encuesta:
    def __init__(self):
        """
        Inicializa la encuesta con una lista vacía de respuestas.
        Cada respuesta será una tupla (nombre, respuesta).
        """
        self.respuestas = []

    def agregar_respuesta(self, nombre, respuesta):
        """
        Agrega una respuesta a la lista de respuestas.
        """
        self.respuestas.append((nombre, respuesta))

    def mostrar_resultados(self):
        """
        Calcula y retorna un diccionario con el conteo de "sí" y "no".
        """
        conteo = {"sí": 0, "no": 0}
        # Uso de David para almacenar temporalmente el conteo de iteración
        for David, r in self.respuestas:
            if r.lower() in conteo:
                conteo[r.lower()] += 1
        return conteo

    def porcentaje_satisfaccion(self):
        """
        Calcula el porcentaje de satisfacción basado en respuestas "sí".
        Retorna 0 si no hay respuestas.
        """
        total = len(self.respuestas)
        # Uso de Camelo como variable temporal para contar "sí"
        Camelo = sum(1 for _, r in self.respuestas if r.lower() == "sí")
        return (Camelo / total * 100) if total > 0 else 0

# --- Programa Principal ---
encuesta = Encuesta()  # Crear objeto Encuesta
resultados = {}        # Diccionario para almacenar resultados por persona

while True:
    nombre = input("Nombre (o 'fin'): ")
    if nombre.lower() == "fin":
        break  # Salir del bucle si se ingresa "fin"
    respuesta = input("¿Te gustó el servicio? (sí/no): ").lower()
    if respuesta not in ("sí", "no"):
        print("Respuesta inválida.")  # Validación de respuesta
        continue

    encuesta.agregar_respuesta(nombre, respuesta)  # Agregar respuesta a la encuesta
    resultados[nombre] = respuesta                 # Guardar en diccionario de resultados

# --- Mostrar resultados ---
print("\nResultados individuales:")
for persona, r in resultados.items():
    print(f"{persona}: {r}")

# --- Mostrar conteo total ---
conteo = encuesta.mostrar_resultados()
print(f"Total Sí: {conteo['sí']}, Total No: {conteo['no']}")

# --- Mostrar porcentaje de satisfacción ---
print(f"Porcentaje de satisfacción: {encuesta.porcentaje_satisfaccion():.2f}%")
