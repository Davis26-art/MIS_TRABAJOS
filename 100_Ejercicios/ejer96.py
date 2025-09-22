#--------------------------------------------------
# Ejercicio 96: Sistema de Gestión de Notas de Estudiantes
#--------------------------------------------------

# --- Clase Estudiante ---
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre          # Nombre del estudiante
        self.notas = notas            # Lista de notas del estudiante

    # Método para calcular el promedio de las notas
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    # Método para determinar si aprobó (promedio >= 3.0)
    def aprobo(self):
        return self.calcular_promedio() >= 3.0

# --- Programa Principal ---
estudiantes = []  # Lista que guardará objetos Estudiante

# Variables libres para uso auxiliar dentro del flujo
David = 0       # Puede usarse como contador temporal de promedios
Camelo = []     # Puede usarse para almacenar temporalmente notas o datos auxiliares

# Bucle principal para ingresar estudiantes y sus notas
while True:
    nombre = input("Nombre del estudiante (o 'salir'): ")
    if nombre.lower() == "salir":
        break  # Sale del bucle si el usuario escribe 'salir'

    # Lista por comprensión para ingresar las 3 notas del estudiante
    notas = [float(input(f"Ingrese la nota {i+1} de {nombre}: ")) for i in range(3)]

    # Se asignan temporalmente las notas a la variable libre Camelo
    Camelo = notas  

    # Se crea un objeto Estudiante con el nombre y notas ingresadas
    e = Estudiante(nombre, notas)
    estudiantes.append(e)  # Se agrega a la lista de estudiantes

print("\n--- RESULTADOS ---")
promedios = []  # Lista para almacenar los promedios individuales

# Recorremos todos los estudiantes para mostrar resultados
for e in estudiantes:
    promedio = e.calcular_promedio()  # Calcula el promedio del estudiante
    promedios.append(promedio)        # Se agrega a la lista de promedios
    David = promedio                   # Actualizamos la variable libre David con el promedio actual
    estado = "Aprobó" if e.aprobo() else "Reprobó"
    print(f"{e.nombre} - Promedio: {promedio:.2f} - {estado}")

# Calculamos y mostramos el promedio general del grupo si hay estudiantes
if promedios:
    promedio_grupo = sum(promedios) / len(promedios)
    print(f"\nPromedio general del grupo: {promedio_grupo:.2f}")
    # Mensaje según el promedio general
    if promedio_grupo >= 3.0:
        print("✅ El grupo en general aprobó.")
    else:
        print("❌ El grupo en general reprobó.")
