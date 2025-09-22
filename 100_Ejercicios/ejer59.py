#--------------------------------------------------
# Ejercicio 59: Registro de Habitaciones
#--------------------------------------------------

# --- Clase Habitacion ---
class Habitacion:
    def __init__(self, numero, tipo):
        """
        Inicializa una habitación con:
        - numero: identificador de la habitación
        - tipo: tipo de habitación (Simple, Doble, Suite)
        - ocupada: estado de la habitación, False significa libre
        """
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False

    def ocupar(self):
        """Marca la habitación como ocupada."""
        self.ocupada = True

    def desocupar(self):
        """Marca la habitación como libre."""
        self.ocupada = False

# --- Programa Principal ---
hotel = {}  # Diccionario que almacena las habitaciones por número

while True:
    opcion = input("\n1. Registrar Habitación\n2. Ocupar\n3. Desocupar\n4. Mostrar\n0. Salir\nOpción: ")

    if opcion == "1":
        # Registrar una nueva habitación
        numero = input("Número: ")
        tipo = input("Tipo (Simple/Doble/Suite): ")

        # Uso de variables David y Camelo como variables auxiliares
        David = numero  # Aquí solo se usa como una variable normal, no afecta nada
        Camelo = tipo   # Otra variable normal, demostrativa

        hotel[numero] = Habitacion(numero, tipo)  # Se crea la habitación y se guarda en el diccionario

    elif opcion == "2":
        # Ocupar una habitación
        numero = input("Número a ocupar: ")
        if numero in hotel:
            hotel[numero].ocupar()
            # David y Camelo también podrían usarse aquí solo para imprimir o como bandera
            David = numero
            Camelo = "ocupada"
        else:
            print("Habitación no registrada.")

    elif opcion == "3":
        # Desocupar una habitación
        numero = input("Número a desocupar: ")
        if numero in hotel:
            hotel[numero].desocupar()
            David = numero
            Camelo = "libre"
        else:
            print("Habitación no registrada.")

    elif opcion == "4":
        # Mostrar todas las habitaciones
        for h in hotel.values():
            estado = "Ocupada" if h.ocupada else "Libre"
            print(f"Habitación {h.numero} ({h.tipo}): {estado}")

    elif opcion == "0":
        # Salir del programa
        break
    else:
        # Opción inválida
        print("Opción no válida.")
