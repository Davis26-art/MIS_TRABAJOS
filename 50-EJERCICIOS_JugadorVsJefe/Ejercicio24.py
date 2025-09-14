#----------------------------------------------
# EJERCICIO 24 -- Generador de usuarios
#----------------------------------------------

import random
import string

# Función para generar un nombre de usuario aleatorio
def generar_usuario(longitud=8, incluir_numeros=True, incluir_guion=False):
    """
    Genera un nombre de usuario con las características especificadas.
    - longitud: cantidad de caracteres
    - incluir_numeros: agrega números si es True
    - incluir_guion: agrega guiones bajos si es True
    """
    caracteres = string.ascii_lowercase  # letras minúsculas
    
    if incluir_numeros:
        caracteres += string.digits  # añadir números
    if incluir_guion:
        caracteres += "_"  # añadir guion bajo
    
    usuario = ""
    for i in range(longitud):
        caracter_aleatorio = random.choice(caracteres)
        usuario += caracter_aleatorio
    return usuario

# Función para evaluar la calidad del nombre de usuario
def evaluar_usuario(usuario):
    """
    Evalúa si el nombre de usuario es fácil de usar y seguro.
    """
    puntos = 0
    comentarios = []

    # Longitud
    if len(usuario) >= 6:
        puntos += 2
        comentarios.append("✔ Longitud adecuada")
    else:
        comentarios.append("✘ Muy corto (mínimo 6 caracteres)")

    # Números
    if any(c.isdigit() for c in usuario):
        puntos += 1
        comentarios.append("✔ Contiene números")
    else:
        comentarios.append("✘ No contiene números")

    # Guion bajo
    if "_" in usuario:
        puntos += 1
        comentarios.append("✔ Contiene guion bajo")
    else:
        comentarios.append("✘ No contiene guion bajo")

    # Resultado de la evaluación
    if puntos >= 4:
        calidad = "Excelente"
    elif puntos >= 3:
        calidad = "Buena"
    elif puntos >= 2:
        calidad = "Aceptable"
    else:
        calidad = "Débil"

    return calidad, comentarios


# Probando el generador de usuarios
print("GENERADOR DE USUARIOS")
print("=" * 40)

usuario1 = generar_usuario(10, True, False)  # letras + números
usuario2 = generar_usuario(8, True, True)    # letras + números + guion
usuario3 = generar_usuario(5, False, False)  # solo letras (corto)

usuarios = [
    ("Usuario estándar (10 caracteres)", usuario1),
    ("Usuario con guion (8 caracteres)", usuario2),
    ("Usuario corto (5 caracteres)", usuario3)
]

# Mostrar resultados
for descripcion, usuario in usuarios:
    calidad, comentarios = evaluar_usuario(usuario)
    print(f"\n{descripcion}:")
    print(f"Nombre de usuario: {usuario}")
    print(f"Calidad: {calidad}")
    for comentario in comentarios:
        print(" ", comentario)
