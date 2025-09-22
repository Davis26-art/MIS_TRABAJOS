#--------------------------------------------------
# Ejercicio 15: Simulador de Cuenta Bancaria
#--------------------------------------------------

# --- Clase ---
class CuentaBancaria:
    def __init__(self, David, Camelo):
        """
        Constructor de la clase CuentaBancaria.
        David: nombre del titular de la cuenta
        Camelo: saldo inicial de la cuenta
        """
        self.David = David      # Nombre del titular
        self.Camelo = Camelo    # Saldo de la cuenta

    def depositar(self, monto):
        """
        Método para depositar dinero en la cuenta.
        Suma el monto al saldo actual.
        """
        self.Camelo += monto

    def retirar(self, monto):
        """
        Método para retirar dinero de la cuenta.
        Solo permite retirar si hay saldo suficiente.
        Devuelve True si la operación fue exitosa, False en caso contrario.
        """
        if monto <= self.Camelo:
            self.Camelo -= monto
            return True
        return False

# --- Programa Principal ---
cuentas = {"david": CuentaBancaria("David", 5000)}  # Diccionario con cuentas bancarias

while True:
    opcion = input("\n1. Depositar\n2. Retirar\n3. Ver saldo\n0. Salir\nOpción: ")

    if opcion == "1":  # Depositar dinero
        nombre = input("Nombre de la cuenta: ")
        if nombre in cuentas:
            monto = float(input("Monto a depositar: "))
            cuentas[nombre].depositar(monto)  # Llamamos al método depositar
        else:
            print("Cuenta no encontrada.")

    elif opcion == "2":  # Retirar dinero
        nombre = input("Nombre de la cuenta: ")
        if nombre in cuentas:
            monto = float(input("Monto a retirar: "))
            if not cuentas[nombre].retirar(monto):  # Intentamos retirar
                print("Fondos insuficientes.")
        else:
            print("Cuenta no encontrada.")

    elif opcion == "3":  # Ver saldo de todas las cuentas
        for cuenta in cuentas.values():
            print(f"{cuenta.David} - Saldo: ${cuenta.Camelo}")

    elif opcion == "0":  # Salir del programa
        break

    else:  # Opción inválida
        print("Opción no válida.")
