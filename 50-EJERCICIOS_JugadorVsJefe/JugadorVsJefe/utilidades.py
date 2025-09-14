# utilidades.py
# --- FUNCIONES DE APOYO ---
# Aquí colocamos funciones pequeñas y reutilizables,
# como mostrar mensajes importantes o manejar recargas.

def mostrar_vida_baja(vida):
    """Muestra un mensaje de alerta si el jugador tiene poca vida."""
    if vida <= 15:
        print("⚠️ ¡ESTÁS EN PELIGRO CRÍTICO! Un golpe más podría ser tu fin...")
