# combate.py
# --- FLUJO PRINCIPAL DEL COMBATE ---
# Aquí está la lógica de turnos, ataques, defensas y comportamiento del jefe.

import random
import jugador
import jefe
import utilidades

turno = 1  # Contador de turnos

def iniciar_combate():
    """
    Maneja el bucle principal del combate:
    - Muestra turnos
    - Pide acción al jugador
    - Aplica efectos del jefe
    - Gestiona recargas
    """

    global turno

    while jugador.vida > 0 and jefe.vida > 0:
        # Avisos de habilidades disponibles
        if jugador.golpe_poderoso_recarga == 0:
            print("✨ ¡Golpe Poderoso Disponible! (G)")
        elif jugador.golpe_poderoso_recarga == 1:
            print("⌛ ¡Golpe Poderoso casi listo! (1 turno restante)")
        if jugador.curacion_emergencia_recarga == 0:
            print("✨ ¡Curación de Emergencia Disponible! (E)")

        # Mostramos estado de vida
        print(f"📅 Turno {turno}")
        print(f"💚 Vida Jugador: {jugador.vida} | 💀 Vida Jefe: {jefe.vida}")
        utilidades.mostrar_vida_baja(jugador.vida)  # ALERTA si la vida es baja

        # Elegimos acción
        accion = input("Elige acción (A=Atacar, C=Curar, D=Defender, G=Golpe Poderoso, E=Curación de Emergencia): ").upper()
        jugador_defiende = False
        critico = random.randint(1, 100) <= jugador.suerte

        # --- ACCIONES DEL JUGADOR ---
        if accion == "A":
            if random.randint(1, 100) <= 15:
                print("😈 El jefe esquivó tu ataque!")
                print("⚡ El jefe contraataca y te hace 7 de daño adicional!")
                jugador.vida -= 7
            else:
                daño = jugador.ataque + (5 if critico else 0)
                if critico:
                    print("💥 ¡Golpe crítico!")
                print(f"🗡️ Golpeas al jefe y haces {daño} de daño.")
                jefe.vida -= daño

        elif accion == "C":
            curacion = random.randint(10, 20)
            jugador.vida += curacion
            print(f"🩹 Te curas {curacion} puntos de vida.")
            print("😈 El jefe aprovecha tu curación para presionarte con un golpe más fuerte!")

        elif accion == "D":
            jugador_defiende = True
            print("🛡️ Te pones en guardia. Recibirás menos daño este turno.")

        elif accion == "G":
            if jugador.golpe_poderoso_recarga == 0:
                if random.randint(1, 100) <= 10:
                    print("❌ ¡Fallaste el Golpe Poderoso!")
                    print("⚡ El jefe aprovecha para contraatacar y te hace 5 de daño.")
                    jugador.vida -= 5
                else:
                    print("⚡ ¡Usas GOLPE PODEROSO!")
                    print("💥 Haces 30 de daño devastador al jefe.")
                    jefe.vida -= 30
                jugador.golpe_poderoso_recarga = 4
            else:
                print("❌ Acción no válida o habilidad en recarga. Pierdes el turno.")

        elif accion == "E":
            if jugador.curacion_emergencia_recarga == 0:
                curacion = random.randint(25, 35)
                jugador.vida += curacion
                print(f"🩺 ¡Curación de EMERGENCIA! Recuperas {curacion} puntos de vida.")
                jugador.curacion_emergencia_recarga = 5
                print("😈 El jefe aprovecha tu curación para presionarte con un golpe más fuerte!")
            else:
                print("❌ Acción no válida o habilidad en recarga. Pierdes el turno.")
        else:
            print("❌ Acción no válida o habilidad en recarga. Pierdes el turno.")

        # --- ACCIONES DEL JEFE ---
        if jefe.vida > 0:
            # Jefe se enfurece al bajar de vida
            if jefe.vida <= 40 and not jefe.enfurecido:
                print("🔥 ¡El jefe se enfurece! Sus ataques son más peligrosos.")
                jefe.ataque += 3
                jefe.enfurecido = True

            golpe_aplastante = random.randint(1, 100) <= 15 and jefe.vida <= 60
            daño_jefe = jefe.ataque

            if turno % 3 == 0:
                print("🔥 El jefe carga un ATAQUE FUERTE!")
                if jugador_defiende and random.randint(1, 100) <= 25:
                    print("💢 ¡El ataque del jefe ROMPE tu defensa!")
                    jugador_defiende = False
                daño_jefe += 3

            if jefe.modo_defensivo:
                daño_jefe = int(daño_jefe * 0.7)
                jefe.modo_defensivo = False

            if golpe_aplastante:
                print("💢 ¡Golpe aplastante! Ignora tu defensa.")
                jugador_defiende = False
                daño_jefe += 8

            if jugador_defiende:
                daño_jefe = int(daño_jefe * 0.5)

            if accion in ["C", "E"]:  # castigo al curarse
                daño_jefe = int(daño_jefe * 1.2)

            print(f"💥 El jefe te golpea y recibes {daño_jefe} de daño.")
            jugador.vida -= daño_jefe

            if random.randint(1, 100) <= 20:
                jefe.modo_defensivo = True
                print("🛡️ El jefe entra en modo defensivo, reduce el daño recibido el próximo turno.")

        # --- RECARGAS ---
        if jugador.golpe_poderoso_recarga > 0:
            jugador.golpe_poderoso_recarga -= 1
        if jugador.curacion_emergencia_recarga > 0:
            jugador.curacion_emergencia_recarga -= 1

        turno += 1
        print()

    # --- RESULTADO FINAL ---
    if jugador.vida <= 0:
        print("☠️ Has sido derrotado por el jefe...")
    else:
        print("🏆 ¡Has vencido al jefe antes de que pueda contraatacar!")
