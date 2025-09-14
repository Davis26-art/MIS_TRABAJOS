#--------------------------------------------------
# EJERCICIO 30 -- Sistema de recomendaciones de comida
#--------------------------------------------------

def calcular_similitud(usuario1, usuario2):
    """
    Calcula similitud entre dos usuarios según sus preferencias de comida.
    Retorna un valor entre 0 (muy diferentes) y 1 (muy similares).
    """
    gustos_comunes = 0
    total_comparaciones = 0

    # Recorremos todas las categorías de usuario1
    for categoria in usuario1:
        if categoria in usuario2:  # Si la categoría también está en el otro usuario
            total_comparaciones += 1
            # Si ambos tienen el mismo gusto (ej: ambos aman o ambos odian la pizza)
            if usuario1[categoria] == usuario2[categoria]:
                gustos_comunes += 1

    if total_comparaciones == 0:
        return 0  # No hay nada en común para comparar

    similitud = gustos_comunes / total_comparaciones
    return round(similitud, 2)


def encontrar_usuarios_similares(usuario_objetivo, base_usuarios, umbral=0.5):
    """
    Encuentra usuarios similares al usuario objetivo en gustos de comida.
    """
    similares = []
    print(f"Buscando usuarios similares a '{usuario_objetivo}'")
    print(f"Umbral de similitud: {umbral}")
    print("-" * 40)

    gustos_objetivo = base_usuarios[usuario_objetivo]

    for nombre_usuario, gustos_usuario in base_usuarios.items():
        if nombre_usuario != usuario_objetivo:  # No comparar consigo mismo
            similitud = calcular_similitud(gustos_objetivo, gustos_usuario)
            print(f"{nombre_usuario}: similitud = {similitud}")
            if similitud >= umbral:
                similares.append((nombre_usuario, similitud))

    # Ordenamos de mayor a menor similitud
    similares.sort(key=lambda x: x[1], reverse=True)
    return similares


def recomendar_comida(usuario_objetivo, usuarios_similares, base_usuarios):
    """
    Recomienda platos de comida basados en lo que les gusta a usuarios similares.
    """
    gustos_objetivo = base_usuarios[usuario_objetivo]
    recomendaciones = {}

    print(f"\nGenerando recomendaciones de comida para '{usuario_objetivo}':")
    for nombre_similar, similitud in usuarios_similares:
        gustos_similar = base_usuarios[nombre_similar]
        print(f"\nAnalizando preferencias de {nombre_similar} (similitud: {similitud}):")
        
        for categoria, le_gusta in gustos_similar.items():
            # Si al usuario similar le gusta algo que el objetivo aún no ha probado
            if categoria not in gustos_objetivo and le_gusta:
                if categoria not in recomendaciones:
                    recomendaciones[categoria] = []
                recomendaciones[categoria].append((nombre_similar, similitud))
                print(f" 👉 Recomendar '{categoria}' (le gusta a {nombre_similar})")

    return recomendaciones


# Base de datos de usuarios y sus preferencias de comida
usuarios = {
    "Ana": {
        "pizza": True, "sushi": True, "hamburguesa": False,
        "ensalada": False, "tacos": True
    },
    "Carlos": {
        "pizza": True, "sushi": False, "hamburguesa": True,
        "ensalada": False, "tacos": True
    },
    "María": {
        "pizza": False, "sushi": True, "hamburguesa": True,
        "ensalada": True, "tacos": False
    },
    "Pedro": {
        "pizza": True, "sushi": True, "hamburguesa": False,
        "ensalada": False, "tacos": False
    },
    "Laura": {
        "pizza": False, "sushi": True, "hamburguesa": True,
        "ensalada": False, "tacos": True
    }
}

print("SISTEMA DE RECOMENDACIONES DE COMIDA")
print("=" * 40)

# Mostrar la base de usuarios
print("Base de usuarios y sus gustos:")
for usuario, gustos in usuarios.items():
    print(f"{usuario}: {gustos}")

print("\n" + "=" * 50)

# Buscar similares para Ana
usuario_objetivo = "Ana"
similares = encontrar_usuarios_similares(usuario_objetivo, usuarios, 0.4)

print(f"\nUsuarios similares a {usuario_objetivo}:")
for similar, similitud in similares:
    print(f" - {similar}: {similitud * 100:.0f}% similar")

# Generar recomendaciones
recomendaciones = recomendar_comida(usuario_objetivo, similares, usuarios)

print(f"\n" + "=" * 30)
print("RECOMENDACIONES FINALES")
print("=" * 30)

if recomendaciones:
    for categoria, recomendadores in recomendaciones.items():
        print(f"\n🍽️ Prueba '{categoria}' (recomendado por {[r[0] for r in recomendadores]})")
else:
    print("No hay recomendaciones disponibles.")
