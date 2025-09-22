#--------------------------------------------------
# Ejercicio 36: Gestión de estudiantes y sus notas
#--------------------------------------------------

# Variables con los nombres David y Camelo
nombre_david = "David"
nombre_camelo = "Camelo"

# --- Clase Estudiante ---
class Estudiante:
    def __init__(self, nombre, notas):
        """
        Constructor de la clase Estudiante.
        - nombre: nombre del estudiante
        - notas: lista de notas del estudiante
        """
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        """
        Calcula el promedio de las notas del estudiante.
        Retorna un valor numérico.
        """
        return sum(self.notas) / len(self.notas)  # suma todas las notas y divide entre la cantidad

    def aprobo(self):
        """
        Determina si el estudiante aprobó.
        Se considera aprobado si el promedio es mayor o igual a 3.0
        Retorna True si aprobó, False si reprobó.
        """
        return self.calcular_promedio() >= 3.0

# --- Programa Principal ---
estudiantes = []  # Lista donde se guardarán los objetos Estudiante

while True:
    # Solicitar el nombre del estudiante
    nombre = input("Nombre del estudiante (o 'salir'): ")
    if nombre.lower() == "salir":  # Salir del bucle si escribe 'salir'
        break

    # Preguntar cuántas notas tendrá el estudiante
    cantidad = int(input(f"¿Cuántas notas tendrá {nombre}? "))
    notas = []  # Lista temporal para guardar las notas del estudiante

    # Bucle para ingresar cada nota
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)  # Agregamos la nota a la lista

    # Crear objeto Estudiante con el nombre y lista de notas
    e = Estudiante(nombre, notas)
    estudiantes.append(e)  # Agregamos el objeto a la lista general

# --- Mostrar resultados ---
print("\n--- RESULTADOS ---")
for e in estudiantes:
    # Determinar estado del estudiante según si aprobó o reprobó
    estado = "Aprobó" if e.aprobo() else "Reprobó"
    # Imprimir nombre, promedio con 2 decimales y estado
    print(f"{e.nombre} - Promedio: {e.calcular_promedio():.2f} - {estado}")

