# ============================
# MANEJO DE ARCHIVOS CON OS
# ============================

import os

# 1. ELIMINAR ARCHIVO
# --------------------
# Verificamos primero si existe 'duc.txt' antes de borrarlo
if os.path.exists('duc.txt'):
    os.remove('duc.txt')
    print("Archivo 'duc.txt' eliminado correctamente.")
else:
    print("El archivo 'duc.txt' no existe, no se puede eliminar.")


# 2. RENOMBRAR ARCHIVO
# --------------------
# Cambiamos el nombre de 'doc.txt' a 'docRename.txt'
if os.path.exists('doc.txt'):
    os.rename('doc.txt', 'docRename.txt')
    print("Archivo 'doc.txt' renombrado a 'docRename.txt'.")
else:
    print("El archivo 'doc.txt' no existe, no se puede renombrar.")
