#--------------------------------------------------
# Ejercicio 34: Encuesta con Porcentaje de Satisfacción
#--------------------------------------------------

# Definimos variables con los nombres David y Camelo
nombre_david = "David"
nombre_camelo = "Camelo"

class Encuesta:
    def __init__(self):
        # Lista para almacenar las respuestas de los participantes
        # Cada elemento será una tupla: (nombre, respuesta)
        self.respuestas = []

    def agregar_respuesta(self, nombre, respuesta):
        """
        Agrega la respuesta de un participante a la lista.
        nombre: str -> nombre del participante
        respuesta: str -> "si" o "no"
        """
        self.respuestas.append((nombre, respuesta))

    def resumen(self):
        """
        Calcula el número de respuestas 'si' y 'no'.
        Retorna un diccionario con conteos: {'si': X, 'no': Y}
        """
        conteo = {"si": 0, "no": 0}
        for _, resp in self.respuestas:
            if resp.lower() == "si":
                conteo["si"] += 1
            elif resp.lower() == "no":
                conteo["no"] += 1
        return conteo

    def porcentaje_satisfaccion(self):
        """
        Calcula el porcentaje de respuestas 'si' sobre el total.
        Retorna un float con el porcentaje.
        """
        total = len(self.respuestas)
        if total == 0:
            return 0
        conteo = self.resumen()
        return (conteo["si"] / total) * 100

# --- Programa Principal ---
# Creamos un objeto Encuesta
encuesta = Encuesta()

# Lista de nombres permitidos, usando las variables definidas
nombres_permitidos = [nombre_david, nombre_camelo]

while True:
    # Pedimos el nombre del participante y capitalizamos la primera letra
    nombre = input(f"Nombre ({nombre_david}/{nombre_camelo} o 'salir'): ").capitalize()
    if nombre.lower() == "salir":
        break
    if nombre not in nombres_permitidos:
        print(f"Solo se permite {nombre_david} o {nombre_camelo}.")
        continue

    # Pedimos la respuesta y validamos
    respuesta = input("¿Te gustó el servicio? (si/no): ").lower()
    if respuesta not in ("si", "no"):
        print("Respuesta no válida.")
        continue

    # Agregamos la respuesta al objeto encuesta
    encuesta.agregar_respuesta(nombre, respuesta)

# Mostrar resultados finales
resultado = encuesta.resumen()
print("\nResumen de la encuesta:")
print(f"Sí: {resultado['si']} - No: {resultado['no']}")
print(f"Porcentaje de satisfacción: {encuesta.porcentaje_satisfaccion():.2f}%")
