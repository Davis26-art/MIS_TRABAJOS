#--------------------------------------------------
# EJERCICIO 33 -- Simulación de crecimiento de vegetación en un terreno
#--------------------------------------------------

import random
import time

def crear_tablero(filas, columnas, densidad=0.3):
    """
    Crea un tablero inicial con plantas (1) y espacios vacíos (0).
    - filas, columnas: dimensiones del terreno.
    - densidad: probabilidad de que una casilla tenga planta al inicio (0..1).
    """
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Si random < densidad colocamos una planta (1), si no, vacío (0)
            esta_viva = 1 if random.random() < densidad else 0
            fila.append(esta_viva)
        tablero.append(fila)
    return tablero

def contar_vecinos_vivos(tablero, fila, columna):
    """
    Cuenta cuántas plantas vivas rodean la casilla (fila, columna).
    Considera las 8 direcciones (incluye diagonales).
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0

    # Movimientos relativos a las 8 celdas alrededor
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),  # arriba-izquierda, arriba, arriba-derecha
        (0, -1),           (0, 1),   # izquierda, derecha
        (1, -1),  (1, 0),  (1, 1)    # abajo-izquierda, abajo, abajo-derecha
    ]

    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        # Verificamos límites para no indexar fuera del tablero
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            vecinos_vivos += tablero[nueva_fila][nueva_columna]
    return vecinos_vivos

def aplicar_reglas(tablero):
    """
    Aplica las reglas de crecimiento/muerte de la vegetación para obtener
    la siguiente generación.
    Reglas (interpretadas para plantas):
      - Planta con < 2 vecinos: muere por aislamiento (no reproduce).
      - Planta con 2 o 3 vecinos: sobrevive (condición estable).
      - Planta con > 3 vecinos: muere por sobrepoblación (competencia).
      - Espacio vacío con exactamente 3 vecinos: nace una planta (dispersión de semillas).
    Retorna:
      - nuevo_tablero: estado actualizado
      - cambios: lista de tuplas (fila, columna, razón) con los cambios ocurridos
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    cambios = []  # guardamos descripciones de lo que ocurrió

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]
            nueva_celula = celula_actual  # por defecto se mantiene

            if celula_actual == 1:  # actualmente hay planta
                if vecinos < 2:
                    nueva_celula = 0
                    cambios.append((i, j, "murió (aislamiento)"))
                elif vecinos > 3:
                    nueva_celula = 0
                    cambios.append((i, j, "murió (sobrepoblación)"))
                else:
                    # 2 o 3 vecinos -> sobrevive (sin cambio)
                    pass
            else:  # casilla vacía
                if vecinos == 3:
                    nueva_celula = 1
                    cambios.append((i, j, "nació (dispersión)"))

            nuevo_tablero[i][j] = nueva_celula

    return nuevo_tablero, cambios

def mostrar_tablero(tablero, generacion, mostrar_coordenadas=False):
    """
    Muestra el terreno en consola.
    - tablero: matriz de 0/1
    - generacion: número actual de generación (para título)
    - mostrar_coordenadas: si True imprime índices (útil para depuración)
    """
    filas = len(tablero)
    columnas = len(tablero[0])

    # Encabezado
    print("\n" + "=" * 60)
    print(f"Generación {generacion} — Vegetación en el terreno")
    print("=" * 60)

    # Mostrar coordenadas de columna si se pide
    if mostrar_coordenadas:
        encabezado = "    " + " ".join(f"{c:2d}" for c in range(columnas))
        print(encabezado)

    # Contadores simples
    total_plantas = 0

    # Imprimir cada fila con un símbolo visual
    for i in range(filas):
        fila_str = ""
        for j in range(columnas):
            if tablero[i][j] == 1:
                fila_str += "🌿 "  # planta representada con emoji
                total_plantas += 1
            else:
                fila_str += ".  "  # punto para terreno vacío
        if mostrar_coordenadas:
            print(f"{i:2d}  {fila_str}")
        else:
            print(fila_str)

    # Estadísticas al final
    print("\nResumen rápido:")
    print(f" Total de casillas: {filas * columnas}")
    print(f" Plantas vivas: {total_plantas}")
    densidad_actual = total_plantas / (filas * columnas)
    print(f" Densidad de plantas: {densidad_actual:.2%}")
    print("=" * 60)

# =========================
# BLOQUE PRINCIPAL: ejecutar una simulación de ejemplo
# =========================
if __name__ == "__main__":
    # Parámetros de la simulación
    filas = 12
    columnas = 30
    densidad_inicial = 0.25   # 25% de casillas con planta al inicio
    max_generaciones = 40
    pausa_segundos = 0.5      # espera entre generaciones para "ver" la animación

    # Crear tablero inicial
    tablero = crear_tablero(filas, columnas, densidad=densidad_inicial)

    # Ciclo principal: mostrar → aplicar reglas → pausar
    for gen in range(1, max_generaciones + 1):
        mostrar_tablero(tablero, gen)
        nuevo_tablero, cambios = aplicar_reglas(tablero)

        # Si no hubo cambios, el sistema llegó a equilibrio — lo avisamos y paramos
        if not cambios:
            print("\nNo hubo cambios en esta generación: el ecosistema se estabilizó.")
            break

        # Mostrar resumen de cambios (si hay pocos, los listamos)
        if len(cambios) <= 8:
            print("\nCambios recientes (fila, col, motivo):")
            for c in cambios:
                print(" ", c)
        else:
            print(f"\nCambios totales en esta generación: {len(cambios)} (no se listan todos)")

        # Preparar siguiente ciclo
        tablero = nuevo_tablero
        time.sleep(pausa_segundos)

    print("\nSimulación finalizada.")
