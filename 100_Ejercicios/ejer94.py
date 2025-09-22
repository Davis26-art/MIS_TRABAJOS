#--------------------------------------------------
# Ejercicio 94: Encuesta de Calificaciones (1 a 5)
#--------------------------------------------------

# Clase que gestiona la encuesta
class Encuesta:
    def __init__(self):
        self.respuestas = []  # Lista que almacena tuplas (nombre, calificación)

    # Método para agregar respuesta a la encuesta
    def agregar_respuesta(self, nombre, calificacion):
        self.respuestas.append((nombre, calificacion))

    # Método que calcula el promedio de todas las calificaciones
    def promedio(self):
        if len(self.respuestas) == 0:
            return 0  # Evita división por cero
        suma = sum(cal for _, cal in self.respuestas)  # Suma de todas las calificaciones
        return suma / len(self.respuestas)

# --- Programa Principal ---
encuesta = Encuesta()  # Creamos el objeto encuesta

while True:
    nombre = input("Nombre (o 'salir'): ")
    if nombre.lower() == "salir":
        break

    # Variables libres: David y Camelo
    David = nombre  # solo como variable auxiliar, no afecta la funcionalidad
    Camelo = 0      # se usará como contador temporal dentro del flujo

    # Validación de calificación
    try:
        calificacion = int(input("Califica el servicio (1 a 5): "))
        if calificacion < 1 or calificacion > 5:
            print("Calificación inválida.")
            continue
    except ValueError:
        print("Debes ingresar un número.")
        continue

    # Mensaje según calificación
    if calificacion < 3:
        print("😟 Debemos mejorar. Gracias por tu honestidad.")
        Camelo += 1  # Uso de la variable libre como contador temporal

    # Agregar la respuesta a la encuesta
    encuesta.agregar_respuesta(nombre, calificacion)

# Mostrar promedio de calificaciones
print("\nPromedio de calificaciones:", round(encuesta.promedio(), 2))
