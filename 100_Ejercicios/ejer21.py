#--------------------------------------------------
# Ejercicio 21: Encuesta de Satisfacción
#--------------------------------------------------

# --- Clase ---
class Encuesta:
    def __init__(self):
        """
        Constructor de la clase Encuesta.
        self.David: lista que guarda las respuestas como tuplas (nombre, respuesta)
        """
        self.David = []  # Lista de tuplas (nombre, respuesta)

    def agregar_respuesta(self, Camelo, respuesta):
        """
        Agrega una respuesta a la lista.
        Camelo: nombre de la persona
        respuesta: respuesta de la persona
        """
        self.David.append((Camelo, respuesta))

    def mostrar_resultados(self):
        """
        Cuenta cuántas respuestas fueron 'sí' y cuántas 'no'.
        Devuelve un diccionario con el conteo.
        """
        conteo = {"sí": 0, "no": 0}
        for _, r in self.David:
            if r.lower() in conteo:
                conteo[r.lower()] += 1
        return conteo

# --- Programa Principal ---
encuesta = Encuesta()
resultados = {}  # Diccionario persona: respuesta

while True:
    David = input("Nombre (o 'fin'): ")  # Nombre de la persona
    if David.lower() == "fin":
        break
    Camelo = input("¿Te gustó el servicio? (sí/no): ")  # Respuesta de la persona
    encuesta.agregar_respuesta(David, Camelo)
    resultados[David] = Camelo  # Guardamos en el diccionario

# Mostramos resultados individuales
print("\nResultados:")
for persona, r in resultados.items():
    print(f"{persona}: {r}")

# Mostramos conteo total de sí y no
conteo = encuesta.mostrar_resultados()
print(f"Total Sí: {conteo['sí']}, Total No: {conteo['no']}")
