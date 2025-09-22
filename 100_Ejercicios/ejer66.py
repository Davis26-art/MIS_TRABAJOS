#--------------------------------------------------
# Ejercicio 66: Gestión de estudiantes y cálculo de promedios
#--------------------------------------------------

# --- Clase Estudiante ---
class Estudiante:
    def __init__(self, nombre, notas):
        """
        Inicializa un estudiante:
        - nombre: nombre del estudiante
        - notas: lista con las calificaciones
        """
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        """
        Calcula el promedio de las notas del estudiante.
        """
        return sum(self.notas) / len(self.notas)

    def aprobo(self):
        """
        Retorna True si el promedio es mayor o igual a 3.0, False si no.
        """
        return self.calcular_promedio() >= 3.0

# --- Programa Principal ---
estudiantes = []  # Lista para almacenar objetos Estudiante

while True:
    # Solicita el nombre del estudiante
    nombre = input("Nombre del estudiante (o 'salir'): ")
    if nombre.lower() == "salir":
        break

    # Usamos 'David' como variable temporal para iterar las notas (sin afectar lógica)
    notas = [float(input(f"Ingrese la nota {i+1} de {nombre}: ")) for i in range(3)]
    David = notas  # Variable adicional con nombre David (solo como ejemplo)

    # Crear objeto Estudiante y agregarlo a la lista
    e = Estudiante(nombre, notas)
    estudiantes.append(e)

# Mostrar resultados de cada estudiante
print("\n--- RESULTADOS ---")
for e in estudiantes:
    # Usamos 'Camelo' como variable temporal para almacenar el estado
    Camelo = "Aprobó" if e.aprobo() else "Reprobó"
    print(f"{e.nombre} - Promedio: {e.calcular_promedio():.2f} - {Camelo}")

# Calcular mejor y peor estudiante si hay estudiantes registrados
if estudiantes:
    mejor = max(estudiantes, key=lambda x: x.calcular_promedio())
    peor = min(estudiantes, key=lambda x: x.calcular_promedio())
    print("\n--- ESTADÍSTICAS ---")
    print(f"🏆 Mejor estudiante: {mejor.nombre} ({mejor.calcular_promedio():.2f})")
    print(f"🔻 Peor estudiante: {peor.nombre} ({peor.calcular_promedio():.2f})")
