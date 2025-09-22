#--------------------------------------------------
# Ejercicio 4: Encuesta de Satisfacción
#--------------------------------------------------

# --- Clase ---
class Encuesta:  # Clase que gestiona las respuestas de la encuesta
    def __init__(self):  # Constructor: se ejecuta al crear el objeto
        self.David = []  # Crea una lista vacía que almacenará tuplas (nombre, respuesta)

    def agregar_respuesta(self, Camelo, respuesta):
        # Agrega una nueva respuesta como tupla a la lista
        # Ejemplo: ("David", "si")
        self.David.append((Camelo, respuesta))

    def resumen(self):
        # Crea un diccionario para contar cuántos "si" y cuántos "no" hubo
        conteo = {"si": 0, "no": 0}
        for _, resp in self.David:  # Recorre cada tupla, solo nos importa resp (la respuesta)
            if resp == "si":
                conteo["si"] += 1  # Suma uno al contador de "si"
            else:
                conteo["no"] += 1  # Suma uno al contador de "no"
        return conteo  # Devuelve el resumen en forma de diccionario

# --- Programa Principal ---
encuesta = Encuesta()  # Se crea un objeto de tipo Encuesta

while True:  # Ciclo para recibir respuestas hasta que el usuario escriba "salir"
    Camelo = input("Nombre (o 'salir'): ")
    if Camelo.lower() == "salir":  # Si escribe "salir" se rompe el bucle
        break

    respuesta = input("¿Te gustó el servicio? (si/no): ").lower()
    if respuesta not in ("si", "no"):  # Validación: solo se aceptan "si" o "no"
        print("Respuesta no válida.")
        continue  # Vuelve al inicio del ciclo para volver a preguntar

    encuesta.agregar_respuesta(Camelo, respuesta)  # Guarda la respuesta en la lista de la encuesta

# Cuando ya no se reciben más respuestas, mostramos el resumen
resultado = encuesta.resumen()  # Llamamos al método que cuenta las respuestas
print("\nResumen:")
print(f"Sí: {resultado['si']} - No: {resultado['no']}")  # Mostramos los resultados finales
