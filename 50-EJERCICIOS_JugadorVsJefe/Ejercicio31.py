#--------------------------------------------------
# EJERCICIO 31 -- Simulación de robots en un entorno
#--------------------------------------------------

import random

# Crea un "robot" como diccionario con sus atributos básicos
def crear_robot(nombre, modelo, energia=100, x=0, y=0):
    return {
        "nombre": nombre,
        "modelo": modelo,
        "energia": energia,   # 0-100: cuánta batería le queda
        "x": x,               # coordenada X en el mapa
        "y": y,               # coordenada Y en el mapa
        "activo": True        # si está operativo (True) o apagado/descargado (False)
    }

# Mueve el robot de forma aleatoria y consume energía por el movimiento
def mover_robot(robot):
    if not robot["activo"]:
        print(f"{robot['nombre']} está inactivo y no puede moverse.")
        return

    dx = random.randint(-1, 1)   # cambio en X: -1, 0 o 1
    dy = random.randint(-1, 1)   # cambio en Y: -1, 0 o 1

    robot["x"] += dx
    robot["y"] += dy
    robot["energia"] -= 5        # moverse cuesta 5 unidades de energía

    print(f"{robot['nombre']} se movió ({dx},{dy}) → posición ({robot['x']},{robot['y']}). Energía: {robot['energia']}")

    if robot["energia"] <= 0:
        robot["energia"] = 0
        robot["activo"] = False
        print(f"⚠️ {robot['nombre']} se quedó sin energía y quedó inactivo.")

# Recarga energía al robot (y lo reactiva si tenía 0)
def recargar(robot, cantidad):
    antes = robot["energia"]
    robot["energia"] += cantidad
    if robot["energia"] > 100:
        robot["energia"] = 100  # tope de batería
    if robot["energia"] > 0:
        robot["activo"] = True
    print(f"{robot['nombre']} recargado: {antes} -> {robot['energia']} (+{cantidad}).")

# El robot realiza una tarea que consume energía distinta según la tarea
def realizar_tarea(robot, tarea):
    costos = {
        "explorar": 10,
        "tomar_foto": 5,
        "analizar_muestra": 15
    }
    costo = costos.get(tarea, 8)  # si la tarea no está en el diccionario, usa 8 por defecto

    if not robot["activo"]:
        print(f"{robot['nombre']} inactivo: no puede realizar '{tarea}'.")
        return

    robot["energia"] -= costo
    print(f"{robot['nombre']} realizó '{tarea}' (-{costo} energía). Energía: {robot['energia']}")

    if robot["energia"] <= 0:
        robot["energia"] = 0
        robot["activo"] = False
        print(f"⚠️ {robot['nombre']} se quedó sin energía durante la tarea.")

# Devuelve una cadena con el estado actual del robot
def estado(robot):
    return f"{robot['nombre']} ({robot['modelo']}) - Energía: {robot['energia']} | Pos: ({robot['x']},{robot['y']}) | Activo: {robot['activo']}"

# Simulación sencilla: crea robots y los opera varios pasos
def simular(pasos=10):
    r1 = crear_robot("R-Scout", "Explorador")
    r2 = crear_robot("Cargo-7", "Soporte", energia=60, x=2, y=-1)
    robots = [r1, r2]

    for paso in range(1, pasos + 1):
        print(f"\n--- Paso {paso} ---")
        for r in robots:
            # 60% de probabilidad de moverse, 40% de hacer una tarea
            if random.random() < 0.6:
                mover_robot(r)
            else:
                tarea = random.choice(["explorar", "tomar_foto", "analizar_muestra"])
                realizar_tarea(r, tarea)

            # Si la batería baja de 30, intentamos recargar (simula estación o recarga remota)
            if r["energia"] < 30 and r["activo"]:
                recargar(r, random.randint(10, 40))

        print("\nEstados al final del paso:")
        for r in robots:
            print(estado(r))

if __name__ == "__main__":
    simular(10)
