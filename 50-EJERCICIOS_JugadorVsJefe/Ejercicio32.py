#--------------------------------------------------
# EJERCICIO 32 -- Simulación de un huerto con plantas
#--------------------------------------------------

import random

# Crear una planta como diccionario (sin clases).
def crear_planta(nombre, especie, agua=50, salud=80):
    """
    Crea y devuelve una planta con atributos básicos:
    - nombre: identificador
    - especie: tipo de planta (ej. 'tomate')
    - agua: nivel de agua 0-100
    - salud: nivel de salud 0-100
    - viva: True si salud>0
    """
    return {
        "nombre": nombre,
        "especie": especie,
        "agua": max(0, min(100, agua)),   # asegurar 0-100
        "salud": max(0, min(100, salud)), # asegurar 0-100
        "viva": True if salud > 0 else False
    }

# Regar la planta: sube agua y mejora un poco la salud
def regar(planta, cantidad):
    # si está muerta, no se puede regar
    if not planta["viva"]:
        print(f"{planta['nombre']} está muerta. No se puede regar.")
        return
    antes_agua = planta["agua"]
    antes_salud = planta["salud"]

    # aumentar agua (tope 100)
    planta["agua"] = min(100, planta["agua"] + cantidad)
    # regar ayuda: 1 punto de salud por cada 10 unidades de agua añadida
    mejora_salud = cantidad // 10
    planta["salud"] = min(100, planta["salud"] + mejora_salud)

    print(f"{planta['nombre']}: agua {antes_agua} -> {planta['agua']}, salud {antes_salud} -> {planta['salud']}")

# Dar luz solar: horas apropiadas mejoran, exceso o falta empeoran
def exponer_luz(planta, horas):
    if not planta["viva"]:
        print(f"{planta['nombre']} inactiva: no recibe luz.")
        return
    antes = planta["salud"]
    if 4 <= horas <= 8:
        planta["salud"] = min(100, planta["salud"] + 5)  # buena cantidad de sol
    elif horas == 0:
        planta["salud"] = max(0, planta["salud"] - 7)   # sin sol: pega fuerte
    else:
        planta["salud"] = max(0, planta["salud"] - 3)   # demasiado o poco sol
    print(f"{planta['nombre']}: salud {antes} -> {planta['salud']} (por {horas}h luz)")
    if planta["salud"] <= 0:
        planta["viva"] = False
        print(f"⚠️ {planta['nombre']} se secó y murió.")

# ¿Necesita riego? True si está viva y el agua está por debajo del umbral
def necesita_riego(planta, umbral=40):
    return planta["viva"] and planta["agua"] < umbral

# Devuelve lista de plantas que necesitan riego en el jardín
def plantas_necesitan_riego(jardin, umbral=40):
    return [p for p in jardin if necesita_riego(p, umbral)]

# Cuenta cuántas plantas hay por especie
def contar_especies(jardin):
    conteo = {}
    for p in jardin:
        conteo[p["especie"]] = conteo.get(p["especie"], 0) + 1
    return conteo

# Lista plantas con salud baja (en riesgo)
def plantas_en_riesgo(jardin, salud_umbral=30):
    return [p for p in jardin if p["viva"] and p["salud"] < salud_umbral]

# Genera un resumen legible del jardín
def resumen_jardin(jardin):
    total = len(jardin)
    especies = contar_especies(jardin)
    avg_agua = sum(p["agua"] for p in jardin) / max(total, 1)
    avg_salud = sum(p["salud"] for p in jardin) / max(total, 1)
    riego = plantas_necesitan_riego(jardin)

    estado_general = "Bueno" if avg_salud > 70 else ("Regular" if avg_salud > 40 else "Malo")

    lines = [
        f"Total plantas: {total}",
        f"Especies (conteo): {especies}",
        f"Agua promedio: {avg_agua:.1f} | Salud promedio: {avg_salud:.1f}",
        f"Plantas que necesitan riego: {len(riego)}",
        f"Estado general del huerto: {estado_general}"
    ]
    return lines

# Simulación simplificada de varios días
def simular_dias(jardin, dias=5):
    """
    Cada día:
    - 30% probabilidad de lluvia (sube agua aleatoriamente)
    - si no llueve, pérdida de agua por evaporación
    - 5% probabilidad pequeña de plaga que baja salud
    - mostramos resumen diario
    """
    for dia in range(1, dias + 1):
        print(f"\n--- Día {dia} ---")
        llueve = random.random() < 0.3
        for p in jardin:
            if not p["viva"]:
                continue

            if llueve:
                subida = random.randint(5, 20)
                p["agua"] = min(100, p["agua"] + subida)
                print(f"Llovió: {p['nombre']} +{subida} agua -> {p['agua']}")
            else:
                perdida = random.randint(3, 8)
                p["agua"] = max(0, p["agua"] - perdida)
                if p["agua"] == 0:
                    p["salud"] = max(0, p["salud"] - 10)  # sequía alta penaliza salud
                # plaga ocasional
                if random.random() < 0.05:
                    daño = random.randint(5, 15)
                    p["salud"] = max(0, p["salud"] - daño)
                    print(f"Plaga: {p['nombre']} -{daño} salud -> {p['salud']}")
                if p["salud"] <= 0:
                    p["viva"] = False
                    print(f"⚠️ {p['nombre']} murió.")

        # breve estado del día
        for p in jardin:
            est = "viva" if p["viva"] else "muerta"
            print(f"- {p['nombre']} ({p['especie']}): agua {p['agua']} | salud {p['salud']} [{est}]")

    print("\n--- Resumen final del huerto ---")
    for linea in resumen_jardin(jardin):
        print(linea)


# Ejemplo de uso directo
if __name__ == "__main__":
    jardin = [
        crear_planta("Tomate1", "tomate", agua=60, salud=85),
        crear_planta("Albahaca", "albahaca", agua=30, salud=70),
        crear_planta("Lechuga", "lechuga", agua=45, salud=65),
        crear_planta("Tomate2", "tomate", agua=20, salud=50)
    ]

    simular_dias(jardin, dias=5)
