# jugador.py
# --- DATOS Y OPCIONES DEL JUGADOR ---
# Aquí guardamos la vida, ataque, defensa y suerte del jugador
# También gestionamos la selección de arma y armadura al inicio.

# --- CONFIGURACIÓN INICIAL DEL JUGADOR ---
vida = 100
ataque = 15
defensa = 5
suerte = 10
golpe_poderoso_recarga = 0
curacion_emergencia_recarga = 0

def seleccionar_equipo():
    """
    Muestra las opciones de armas y armaduras al jugador
    y ajusta sus estadísticas según la elección.
    """
    global ataque, suerte, defensa

    print("⚔️ SELECCIÓN DE EQUIPO ⚔️")
    print("Armas: 1) Espada Equilibrada  2) Gran Espada (+5 ATQ, -5 SUE)  3) Daga Ágil (-5 ATQ, +10 SUE)")
    arma = input("Elige arma (1/2/3): ")
    if arma == "2":
        ataque += 5
        suerte -= 5
    elif arma == "3":
        ataque -= 5
        suerte += 10

    print("Armaduras: 1) Pesada (+5 DEF, -10 SUE)  2) Ligera (-3 DEF, +10 SUE)  3) Sin armadura")
    armadura = input("Elige armadura (1/2/3): ")
    if armadura == "1":
        defensa += 5
        suerte -= 10
    elif armadura == "2":
        defensa -= 3
        suerte += 10
