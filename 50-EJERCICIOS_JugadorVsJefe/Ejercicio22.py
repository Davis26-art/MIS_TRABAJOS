#----------------------------------------------
# EJERCICIO 22 -- Funciones con notas
#----------------------------------------------

# Función para calcular el promedio de 3 notas
def promedio(n1, n2, n3):
    """Recibe tres notas y devuelve el promedio"""
    resultado = (n1 + n2 + n3) / 3
    return resultado

# Función para verificar si el estudiante aprueba
def aprobar(prom):
    """Recibe un promedio y devuelve si aprueba o no"""
    if prom >= 3.0:  # Condición mínima de aprobación
        return "Aprobado ✅"
    else:
        return "Reprobado ❌"

# Probando con un estudiante
nota1 = 4.0
nota2 = 2.8
nota3 = 3.5

print("SISTEMA DE NOTAS CON FUNCIONES")
print(f"Notas del estudiante: {nota1}, {nota2}, {nota3}")
print("-" * 40)

# Usamos la función promedio
prom = promedio(nota1, nota2, nota3)
print(f"Promedio final: {prom:.2f}")  # .2f limita a 2 decimales

# Usamos la función aprobar
print("Resultado final:", aprobar(prom))

# También podemos probar directamente otras combinaciones
print("\nOTROS EJEMPLOS:")
print("Promedio de 2.0, 3.0, 2.5 =", promedio(2.0, 3.0, 2.5), "->", aprobar(promedio(2.0, 3.0, 2.5)))
print("Promedio de 4.5, 4.0, 5.0 =", promedio(4.5, 4.0, 5.0), "->", aprobar(promedio(4.5, 4.0, 5.0)))
