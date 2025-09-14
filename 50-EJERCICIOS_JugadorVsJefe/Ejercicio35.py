#--------------------------------------------------
# EJERCICIO 35 -- Simulación y compresión de melodías musicales
#--------------------------------------------------

import random

def crear_melodia(longitud, notas=None, prob_repetir=0.25):
    """
    Crea una lista de 'notas' (ej. 'C','D','E') de la longitud indicada.
    prob_repetir: probabilidad de repetir la nota anterior (genera runs).
    Retorna: ['C','C','D','E',...]
    """
    if notas is None:
        notas = ['C','D','E','F','G','A','B']  # escala simple
    if longitud <= 0:
        return []
    melodia = []
    # primera nota al azar
    melodia.append(random.choice(notas))
    # para el resto, a veces repetimos la nota anterior (para crear secuencias)
    for _ in range(1, longitud):
        if random.random() < prob_repetir:
            melodia.append(melodia[-1])     # repetir
        else:
            melodia.append(random.choice(notas))
    return melodia

def comprimir_rle(melodia):
    """
    Compresión por run-length encoding (RLE).
    Entrada: ['C','C','C','D','D','E']
    Salida: [(3,'C'), (2,'D'), (1,'E')]
    """
    if not melodia:
        return []
    comprimido = []
    actual = melodia[0]
    cuenta = 1
    for nota in melodia[1:]:
        if nota == actual:
            cuenta += 1
        else:
            comprimido.append((cuenta, actual))  # guardar run terminado
            actual = nota
            cuenta = 1
    comprimido.append((cuenta, actual))        # guardar último run
    return comprimido

def descomprimir_rle(comprimido):
    """
    Convierte [(3,'C'), (2,'D')] de vuelta a ['C','C','C','D','D'].
    """
    des = []
    for cuenta, nota in comprimido:
        des.extend([nota] * cuenta)
    return des

def contar_frecuencias(melodia):
    """
    Cuenta cuántas veces aparece cada nota (sin usar Counter).
    Retorna: (diccionario nota->conteo, nota_mas_frecuente, su_conteo)
    """
    freqs = {}
    for nota in melodia:
        freqs[nota] = freqs.get(nota, 0) + 1
    # hallar la más frecuente (si hay empate, devuelve la primera encontrada)
    nota_top = None
    cuenta_top = 0
    for n, c in freqs.items():
        if c > cuenta_top:
            nota_top = n
            cuenta_top = c
    return freqs, nota_top, cuenta_top

def resumen_melodia(melodia, comprimido):
    """
    Genera líneas de texto con estadísticas útiles:
    - total notas, notas únicas, nota más frecuente,
    - cantidad de bloques en la compresión y ratio.
    """
    total = len(melodia)
    if total == 0:
        return ["Melodía vacía."]
    unicas = len(set(melodia))
    _, nota_top, cuenta_top = contar_frecuencias(melodia)
    bloques = len(comprimido)
    ratio = round(bloques / total, 3)
    lines = [
        f"Total notas: {total}",
        f"Notas únicas: {unicas}",
        f"Nota más frecuente: '{nota_top}' ({cuenta_top} veces)",
        f"Bloques (runs) en compresión: {bloques}",
        f"Ratio bloques/nota: {ratio}  (cuanto más pequeño, mejor la compresión)"
    ]
    return lines

def simular_melodia(longitud=30, prob_repetir=0.25):
    """
    Genera una melodía, la comprime (RLE), la descomprime y muestra resultados.
    """
    mel = crear_melodia(longitud, prob_repetir=prob_repetir)
    print("Melodía generada:")
    print(" ".join(mel))

    comprimido = comprimir_rle(mel)
    # representación compacta tipo "3C 2D 1E"
    comp_str = " ".join(f"{cnt}{nota}" for cnt, nota in comprimido)
    print("\nMelodía comprimida (RLE):")
    print(comp_str)

    des = descomprimir_rle(comprimido)
    # comprobación simple: la descompresión debe dar exactamente la original
    if des == mel:
        print("\nDescompresión verificada: OK")
    else:
        print("\n⚠️ Error: la descompresión no coincide con la original (algo falló)")

    print("\nResumen:")
    for line in resumen_melodia(mel, comprimido):
        print("- " + line)

# Ejemplo de uso directo
if __name__ == "__main__":
    # prueba con más probabilidad de repeticiones para ver compresión efectiva
    simular_melodia(longitud=40, prob_repetir=0.35)
