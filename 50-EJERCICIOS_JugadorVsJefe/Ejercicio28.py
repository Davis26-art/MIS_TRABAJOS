#--------------------------------------------------
# EJERCICIO 28 -- Contador de frecuencias y estadísticas
#--------------------------------------------------

def contar_frecuencias(lista):
    """
    Cuenta cuántas veces se repite cada color en la lista
    Retorna un diccionario con color: frecuencia
    """
    frecuencias = {}  # Diccionario para almacenar resultados
    print(f"Analizando respuestas: {lista}")
    print("\nProceso de conteo:")

    for color in lista:                     # Recorremos cada color en la lista
        if color in frecuencias:            # Si el color ya está en el diccionario
            frecuencias[color] += 1         # Aumentamos su frecuencia en 1
            print(f" {color}: incrementado a {frecuencias[color]}")
        else:                               # Si el color aparece por primera vez
            frecuencias[color] = 1
            print(f" {color}: primer aparición")
    return frecuencias


def encontrar_mas_frecuente(frecuencias):
    """Encuentra el color que más se repite"""
    if not frecuencias:                     # Si el diccionario está vacío
        return None, 0
    color_max = max(frecuencias, key=frecuencias.get)   # Busca el color con mayor frecuencia
    frecuencia_max = frecuencias[color_max]
    return color_max, frecuencia_max


def mostrar_estadisticas(frecuencias):
    """Muestra estadísticas detalladas"""
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE COLORES FAVORITOS")
    print("=" * 40)

    # Ordenamos los colores por frecuencia (mayor a menor)
    frecuencias_ordenadas = sorted(frecuencias.items(),
                                   key=lambda x: x[1],
                                   reverse=True)

    total_respuestas = sum(frecuencias.values())     # Total de respuestas dadas
    colores_unicos = len(frecuencias)                # Número de colores distintos

    print(f"Total de respuestas: {total_respuestas}")
    print(f"Colores únicos: {colores_unicos}")

    print("\nFrecuencias (ordenadas por cantidad):")
    for color, frecuencia in frecuencias_ordenadas:
        porcentaje = (frecuencia / total_respuestas) * 100
        barra = "█" * frecuencia                     # Gráfico de barras simple
        print(f" {color:>7}: {frecuencia:>2} veces ({porcentaje:4.1f}%) {barra}")

    # Color más votado
    mas_frecuente, max_freq = encontrar_mas_frecuente(frecuencias)
    print(f"\n🎯 Color más elegido: {mas_frecuente} ({max_freq} veces)")


# Probando el contador de frecuencias con una encuesta
print("ENCUESTA DE COLORES FAVORITOS")
print("=" * 35)

# Lista de respuestas de varias personas
respuestas = ["azul", "rojo", "verde", "azul", "rojo", "azul",
              "amarillo", "rojo", "verde", "azul", "rojo"]

# Contamos frecuencias
frecuencias_colores = contar_frecuencias(respuestas)

# Mostramos estadísticas
mostrar_estadisticas(frecuencias_colores)
