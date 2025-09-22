#--------------------------------------------------
# Ejercicio 60: IMC con Clasificación
#--------------------------------------------------

# --- Clase Persona ---
class Persona:
    def __init__(self, nombre, peso, altura):
        """
        Inicializa una persona con:
        - nombre: nombre de la persona
        - peso: en kilogramos
        - altura: en metros
        """
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        """
        Calcula el IMC (Índice de Masa Corporal) usando la fórmula:
        IMC = peso / (altura^2)
        """
        return self.peso / (self.altura ** 2)

    def clasificar_imc(self):
        """
        Clasifica el IMC según los rangos estándar:
        - Bajo peso < 18.5
        - Normal 18.5 - 24.9
        - Sobrepeso 25 - 29.9
        - Obesidad >= 30
        """
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"

# --- Programa Principal ---
personas = []     # Lista de objetos Persona
resultados = {}   # Diccionario nombre: (IMC, clasificación)

while True:
    nombre = input("Nombre (o 'fin'): ")
    if nombre.lower() == "fin":
        break

    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    # Crear objeto Persona
    p = Persona(nombre, peso, altura)
    personas.append(p)

    # --- Uso de variables David y Camelo ---
    # David se usa como variable temporal para almacenar el IMC calculado
    David = p.calcular_imc()
    # Camelo se usa como variable temporal para almacenar la clasificación
    Camelo = p.clasificar_imc()
    # Fin de uso, se agregan al diccionario de resultados
    resultados[nombre] = (David, Camelo)

# --- Mostrar resultados ---
print("\nResultados:")
for nombre, (imc, clasificacion) in resultados.items():
    print(f"{nombre}: IMC = {imc:.2f} ({clasificacion})")
