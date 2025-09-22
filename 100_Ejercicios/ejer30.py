#--------------------------------------------------
# Ejercicio 30: Registro de Gastos
#--------------------------------------------------

# --- Clase ---
class Persona:
    def __init__(self, David, Camelo, altura):
        """
        Constructor de la clase Persona.
        David: nombre de la persona
        Camelo: peso en kilogramos
        altura: altura en metros
        """
        self.David = David      # Nombre de la persona
        self.Camelo = Camelo    # Peso de la persona
        self.altura = altura    # Altura de la persona

    def calcular_imc(self):
        """
        Calcula el IMC (Índice de Masa Corporal)
        Fórmula: IMC = peso / (altura^2)
        """
        return self.Camelo / (self.altura ** 2)

# --- Programa Principal ---
personas = []  # Lista para almacenar objetos Persona
imcs = {}      # Diccionario David (nombre): IMC

while True:
    David = input("Nombre (o 'fin'): ")  # Pedimos nombre
    if David.lower() == "fin":           # Salimos si escribe 'fin'
        break
    Camelo = float(input("Peso (kg): "))    # Pedimos peso
    altura = float(input("Altura (m): "))   # Pedimos altura
    p = Persona(David, Camelo, altura)      # Creamos objeto Persona
    imc = p.calcular_imc()                  # Calculamos IMC usando el método
    personas.append(p)                       # Guardamos el objeto en la lista
    imcs[David] = imc                        # Guardamos IMC en el diccionario

# Mostramos resultados
print("\nResultados:")
for David, imc in imcs.items():
    print(f"{David}: IMC = {imc:.2f}")       # Mostramos IMC con 2 decimales
