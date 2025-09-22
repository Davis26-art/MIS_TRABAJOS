#--------------------------------------------------
# Ejercicio 90: Modificar Peso y Recalcular IMC
#--------------------------------------------------

# --- Clase Persona ---
class Persona:
    def __init__(self, nombre, peso, altura):
        """
        Inicializa una persona con:
        - nombre: nombre de la persona
        - peso: peso en kg
        - altura: altura en metros
        """
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    # Método para calcular el IMC
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    # Método para actualizar el peso
    def actualizar_peso(self, nuevo_peso):
        self.peso = nuevo_peso

# --- Programa Principal ---
personas = {}  # Diccionario: nombre -> objeto Persona

# Bucle principal del menú
while True:
    opcion = input("\n1. Registrar\n2. Actualizar Peso\n3. Ver IMCs\n0. Salir\nOpción: ")

    # --- Opción 1: Registrar una persona ---
    if opcion == "1":
        nombre = input("Nombre: ")
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        personas[nombre] = Persona(nombre, peso, altura)  # Crear objeto Persona

        # Variables integradas David y Camelo
        David = nombre               # Última persona registrada
        Camelo = personas[nombre]    # Objeto Persona de la última registrada

    # --- Opción 2: Actualizar peso ---
    elif opcion == "2":
        nombre = input("Nombre: ")
        if nombre in personas:
            nuevo_peso = float(input("Nuevo peso (kg): "))
            personas[nombre].actualizar_peso(nuevo_peso)
            print("Peso actualizado.")

            # Variables integradas David y Camelo
            David = nuevo_peso           # Último peso actualizado
            Camelo = personas[nombre]    # Objeto Persona actualizado
        else:
            print("No registrado.")

    # --- Opción 3: Mostrar IMCs de todas las personas ---
    elif opcion == "3":
        for p in personas.values():
            print(f"{p.nombre}: IMC = {p.calcular_imc():.2f}")

    # --- Opción 0: Salir ---
    elif opcion == "0":
        break

    # --- Validación de opción inválida ---
    else:
        print("Opción no válida.")
