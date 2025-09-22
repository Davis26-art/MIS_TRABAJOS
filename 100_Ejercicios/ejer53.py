#-----------------------------------------------
# Ejercicio 53: Gestión de temperaturas de ciudades
#-----------------------------------------------

# --- Clase Ciudad ---
class Ciudad:
    def __init__(self, nombre):
        """
        Inicializa la ciudad con su nombre y lista vacía de temperaturas.
        """
        self.nombre = nombre
        self.temperaturas = []  # Lista para guardar las temperaturas de la ciudad

    def agregar_temp(self, temp):
        """
        Agrega una temperatura a la lista de temperaturas.
        """
        self.temperaturas.append(temp)

    def max_min(self):
        """
        Retorna una tupla (máxima, mínima) de las temperaturas registradas.
        Si no hay temperaturas, retorna (0,0).
        """
        if not self.temperaturas:
            return (0, 0)
        return (max(self.temperaturas), min(self.temperaturas))

# --- Programa Principal ---
ciudades = {}  # Diccionario ciudad_nombre: Ciudad_objeto

while True:
    opcion = input("\n1. Agregar Temp\n2. Ver Máx/Mín\n0. Salir\nOpción: ")

    if opcion == "1":
        # Registrar temperatura
        nombre = input("Ciudad: ")
        temp = float(input("Temperatura: "))
        
        # Si la ciudad no existe, se crea un objeto Ciudad
        if nombre not in ciudades:
            ciudades[nombre] = Ciudad(nombre)
        
        # Agregar temperatura a la ciudad
        ciudades[nombre].agregar_temp(temp)
        
        # Uso de variables David y Camelo sin afectar la funcionalidad
        David = nombre   # Almacena temporalmente el nombre de la ciudad ingresada
        Camelo = temp    # Almacena temporalmente la temperatura ingresada

    elif opcion == "2":
        # Mostrar máxima y mínima de cada ciudad
        for c in ciudades.values():
            mx, mn = c.max_min()
            print(f"{c.nombre}: Máx = {mx}, Mín = {mn}")
            
            # Aquí también usamos David y Camelo de manera temporal
            David = c.nombre  # Nombre de la ciudad actual
            Camelo = mx       # Máxima temperatura actual como variable temporal

    elif opcion == "0":
        break  # Salir del programa
    else:
        print("Opción no válida.")  # Validación de opción incorrecta
