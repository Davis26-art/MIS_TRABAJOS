#--------------------------------------------------
# EJERCICIO 34 -- Optimización de rutas para drones de reparto
#--------------------------------------------------

import random

# -------------------------
# Funciones básicas
# -------------------------

def crear_puntos(num_puntos, x_max=100, y_max=100):
    """
    Crea una lista de coordenadas (x, y) aleatorias.
    Cada punto representa una dirección de entrega para los drones.
    """
    puntos = []
    for i in range(num_puntos):
        x = random.randint(0, x_max)
        y = random.randint(0, y_max)
        puntos.append((x, y))
    return puntos

def calcular_distancia(p1, p2):
    """
    Distancia euclidiana entre dos puntos p1 y p2.
    No usamos math: usamos **0.5 para la raíz cuadrada.
    Devuelve un float redondeado a 2 decimales.
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    distancia = (dx*dx + dy*dy) ** 0.5
    return round(distancia, 2)

def calcular_distancia_total_ruta(puntos, ruta):
    """
    Suma las distancias entre ciudades consecutivas siguiendo 'ruta'.
    La ruta vuelve al punto inicial (circuito cerrado).
    'ruta' es una lista de índices de 'puntos'.
    """
    total = 0.0
    n = len(ruta)
    for i in range(n):
        a = puntos[ruta[i]]
        b = puntos[ruta[(i + 1) % n]]  # siguiente, con vuelta al inicio
        total += calcular_distancia(a, b)
    return round(total, 2)

# -------------------------
# Heurística simple: vecino más cercano (greedy)
# -------------------------

def metodo_greedy(puntos, inicio=0):
    """
    Construye una ruta empezando en 'inicio' y siempre yendo al
    punto no visitado más cercano (nearest neighbor).
    Es rápido y simple; no garantiza óptimo global pero funciona bien para pocos minutos de café.
    """
    n = len(puntos)
    visitado = [False] * n
    ruta = [inicio]
    visitado[inicio] = True
    actual = inicio

    for _ in range(n - 1):
        mejor = None
        mejor_dist = float('inf')
        for j in range(n):
            if not visitado[j]:
                d = calcular_distancia(puntos[actual], puntos[j])
                if d < mejor_dist:
                    mejor_dist = d
                    mejor = j
        ruta.append(mejor)
        visitado[mejor] = True
        actual = mejor

    return ruta

# -------------------------
# Mejora local simple: 2-opt básico
# -------------------------

def mejorar_2opt(ruta, puntos, max_iter=100):
    """
    Intenta mejorar la ruta con un 2-opt local:
    intercambia segmentos para ver si la distancia total baja.
    Repite hasta no encontrar mejoras o llegar a max_iter iteraciones.
    """
    mejor_ruta = ruta[:]
    mejor_dist = calcular_distancia_total_ruta(puntos, mejor_ruta)
    it = 0
    improved = True

    while improved and it < max_iter:
        improved = False
        it += 1
        n = len(mejor_ruta)
        # probar todas las parejas i<j y revertir el segmento entre ellas
        for i in range(1, n - 1):          # empieza en 1 para mantener el origen fijo opcionalmente
            for j in range(i + 1, n):
                if j - i == 0:
                    continue
                nueva = mejor_ruta[:]
                nueva[i:j] = reversed(nueva[i:j])  # intercambio 2-opt
                nueva_dist = calcular_distancia_total_ruta(puntos, nueva)
                if nueva_dist < mejor_dist:
                    # si mejoró, aceptamos y rompemos para reiniciar búsqueda
                    mejor_ruta = nueva
                    mejor_dist = nueva_dist
                    improved = True
                    break
            if improved:
                break

    return mejor_ruta

# -------------------------
# Utilidades de salida
# -------------------------

def mostrar_puntos(puntos):
    """Imprime la lista de puntos con índices y coordenadas."""
    for i, (x, y) in enumerate(puntos):
        print(f"{i}: ({x}, {y})")

def mostrar_ruta(puntos, ruta, titulo="Ruta"):
    """
    Imprime la ruta en orden (índice -> coordenada) y la distancia total.
    """
    print(f"\n{titulo}:")
    for idx in ruta:
        x, y = puntos[idx]
        print(f"  {idx} -> ({x},{y})")
    total = calcular_distancia_total_ruta(puntos, ruta)
    print(f"Distancia total: {total} unidades")

# -------------------------
# Ejecución principal
# -------------------------

if __name__ == "__main__":
    # generar puntos de entrega aleatorios (drone delivery)
    puntos = crear_puntos(8, x_max=100, y_max=100)  # 8 direcciones: suficiente para probar
    print("Puntos (direcciones) generadas:")
    mostrar_puntos(puntos)

    # obtener ruta inicial por heurística greedy
    ruta_greedy = metodo_greedy(puntos, inicio=0)
    mostrar_ruta(puntos, ruta_greedy, titulo="Ruta greedy inicial")

    # intentar mejorar con 2-opt
    ruta_mejorada = mejorar_2opt(ruta_greedy, puntos, max_iter=200)
    mostrar_ruta(puntos, ruta_mejorada, titulo="Ruta después de 2-opt (mejora local)")

    # comparación rápida: si mejoró, lo decimos sin drama
    d_ini = calcular_distancia_total_ruta(puntos, ruta_greedy)
    d_mej = calcular_distancia_total_ruta(puntos, ruta_mejorada)
    print(f"\nComparación: inicial {d_ini} -> mejorada {d_mej} (ahorraste {round(d_ini - d_mej,2)} unidades)")
