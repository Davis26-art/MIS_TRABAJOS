# main.py
# --- PUNTO DE ENTRADA DEL JUEGO ---
# Aquí simplemente se conecta todo: jugador, jefe y el flujo de combate.

import jugador
import combate

# --- CONFIGURACIÓN INICIAL ---
# Pedimos al jugador que elija su equipo (arma y armadura)
jugador.seleccionar_equipo()

print("\n⚔️ ¡COMBATE INICIADO!\n")

# --- INICIO DEL COMBATE ---
# Llamamos a la función que maneja los turnos y las acciones
combate.iniciar_combate()
