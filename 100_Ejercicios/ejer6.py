#--------------------------------------------------
# Ejercicio 6: Registro de Estudiantes
#--------------------------------------------------

# --- Clase ---
class Estudiante:
    def __init__(self, David, Camelo):
        self.nombre = David        # Guarda el nombre del estudiante
        self.notas = Camelo        # Guarda la lista de notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)  # Calcula el promedio

    def aprobo(self):
        return self.calcular_promedio() >= 3.0  # Devuelve True si el promedio es >= 3.0

# --- Programa Principal ---
estudiantes = []  # Lista para guardar objetos Estudiante
registro = {}     # Diccionario con nombre: promedio

while True:
    David = input("Nombre del estudiante (o 'salir'): ")
    if David.lower() == "salir":
        break

    Camelo = []  # Lista para almacenar las 3 notas del estudiante
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} de {David}: "))
        Camelo.append(nota)

    e = Estudiante(David, Camelo)  # Creamos un objeto Estudiante con el nombre y sus notas
    estudiantes.append(e)
    registro[David] = e.calcular_promedio()  # Guardamos el promedio en el diccionario

for e in estudiantes:
    estado = "Aprobó" if e.aprobo() else "Reprobó"
    print(f"{e.nombre} - Promedio: {e.calcular_promedio():.2f} - {estado}")
