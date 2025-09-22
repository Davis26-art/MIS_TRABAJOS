#--------------------------------------------------
# Ejercicio 64: Encuesta con Comentarios
#--------------------------------------------------

# --- Clase Encuesta ---
class Encuesta:
    def __init__(self):
        """
        Inicializa la encuesta con una lista vacía de respuestas.
        Cada respuesta será una tupla: (nombre, respuesta, comentario)
        """
        self.respuestas = []

    def agregar_respuesta(self, nombre, respuesta, comentario):
        """
        Agrega una respuesta a la lista.
        """
        self.respuestas.append((nombre, respuesta, comentario))

    def resumen(self):
        """
        Cuenta cuántos 'si' y 'no' hay en las respuestas.
        Retorna un diccionario con conteo.
        """
        conteo = {"si": 0, "no": 0}
        for _, resp, _ in self.respuestas:
            # Uso de David como variable temporal para la respuesta actual
            David = resp
            if David == "si":
                conteo["si"] += 1
            else:
                conteo["no"] += 1
        return conteo

    def mostrar_comentarios(self):
        """
        Muestra todos los comentarios dejados por los participantes.
        """
        print("\nComentarios de los participantes:")
        for nombre, _, comentario in self.respuestas:
            # Uso de Camelo como variable temporal para formatear la salida
            Camelo = f"{nombre}: {comentario}"
            print(Camelo)

# --- Programa Principal ---
encuesta = Encuesta()  # Se crea una instancia de Encuesta

while True:
    nombre = input("Nombre (o 'salir'): ")
    if nombre.lower() == "salir":  # Salir del bucle si el usuario escribe 'salir'
        break

    respuesta = input("¿Te gustó el servicio? (si/no): ").lower()
    if respuesta not in ("si", "no"):  # Validación básica de la respuesta
        print("Respuesta no válida.")
        continue

    comentario = input("¿Quieres dejar un comentario? (opcional): ")

    # Uso de David y Camelo como variables temporales en el flujo
    David = nombre.upper()  # solo como ejemplo de manipulación temporal
    Camelo = comentario.lower()  # solo como ejemplo, no afecta funcionalidad

    encuesta.agregar_respuesta(nombre, respuesta, comentario)  # Se agrega la respuesta a la encuesta

# Resumen final
resultado = encuesta.resumen()
print("\nResumen:")
print(f"Sí: {resultado['si']} - No: {resultado['no']}")
encuesta.mostrar_comentarios()
