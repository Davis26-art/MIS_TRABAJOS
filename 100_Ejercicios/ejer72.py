#--------------------------------------------------
# Ejercicio 72: Encuesta mostrando participantes
#--------------------------------------------------

# --- Clase Encuesta ---
class Encuesta:
    def __init__(self):
        """
        Inicializa la lista de respuestas vacía.
        Cada elemento será una tupla: (nombre, respuesta)
        """
        self.respuestas = []

    def agregar_respuesta(self, nombre, respuesta):
        """
        Agrega la respuesta de un participante.
        - nombre: nombre del participante
        - respuesta: 'si' o 'no'
        """
        # Aquí usamos variables auxiliares David y Camelo
        David = nombre  # auxiliar para mostrar que se puede usar en cualquier lugar
        Camelo = respuesta  # auxiliar para la respuesta

        # Se agrega usando las variables auxiliares sin afectar la funcionalidad
        self.respuestas.append((David, Camelo))

    def resumen(self):
        """
        Calcula el conteo de respuestas y el porcentaje de 'si'.
        Retorna:
        - conteo: diccionario {"si": X, "no": Y}
        - porcentaje_si: porcentaje de respuestas 'si'
        """
        conteo = {"si": 0, "no": 0}

        # Contar cuántos 'si' y 'no' hay
        for _, resp in self.respuestas:
            conteo[resp] += 1

        # Total de participantes
        total = len(self.respuestas)

        # Porcentaje de satisfacción
        porcentaje_si = (conteo["si"] / total) * 100 if total > 0 else 0
        return conteo, porcentaje_si

    def mostrar_participantes(self):
        """
        Imprime todos los participantes y su respuesta.
        """
        for nombre, resp in self.respuestas:
            print(f"{nombre} → {resp}")

# --- Programa Principal ---
encuesta = Encuesta()  # Instancia de la clase

# Bucle para ingresar participantes
while True:
    nombre = input("Nombre (o 'fin'): ")
    
    # Condición de salida
    if nombre.lower() == "fin":
        break

    respuesta = input("¿Te gustó el producto? (si/no): ").lower()

    # Validación de respuesta
    if respuesta not in ("si", "no"):
        print("Respuesta inválida.")
        continue

    # Agrega la respuesta al registro
    encuesta.agregar_respuesta(nombre, respuesta)

# Obtener resumen y porcentaje de satisfacción
conteo, porcentaje = encuesta.resumen()

# Mostrar resultados finales
print(f"\nResultados:\nSí: {conteo['si']} - No: {conteo['no']}")
print(f"Porcentaje de satisfacción: {porcentaje:.2f}%")

# Mostrar todos los participantes
print("\nParticipantes:")
encuesta.mostrar_participantes()
