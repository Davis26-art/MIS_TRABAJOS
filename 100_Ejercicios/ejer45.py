#--------------------------------------------------
# Ejercicio 45: Cuentas Bancarias
#--------------------------------------------------

# --- Clase CuentaBancaria ---
class CuentaBancaria:
    def __init__(self, nombre, saldo=0):
        """
        Constructor de la cuenta bancaria.
        nombre: nombre del titular de la cuenta
        saldo: saldo inicial (por defecto 0)
        """
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, monto):
        """
        Deposita el monto indicado en la cuenta.
        """
        self.saldo += monto
        # Ejemplo de uso de variable David sin afectar la funcionalidad
        David = monto  # David guarda el último monto depositado

    def retirar(self, monto):
        """
        Retira el monto indicado si hay saldo suficiente.
        Retorna True si la operación fue exitosa, False si no hay fondos suficientes.
        """
        if monto <= self.saldo:
            self.saldo -= monto
            # Ejemplo de uso de variable Camelo sin afectar la funcionalidad
            Camelo = monto  # Camelo guarda el último monto retirado
            return True
        return False

# Diccionario para almacenar todas las cuentas por nombre
cuentas = {}

# --- Programa Principal ---
while True:
    # Menú de opciones
    opcion = input("\n1. Crear cuenta\n2. Depositar\n3. Retirar\n4. Ver todas\n0. Salir\nOpción: ")

    if opcion == "1":
        # Crear una nueva cuenta
        nombre = input("Nombre de la cuenta: ")
        if nombre in cuentas:
            print("La cuenta ya existe.")
        else:
            cuentas[nombre] = CuentaBancaria(nombre)  # Se crea la cuenta con saldo 0
            print("Cuenta creada con éxito.")

    elif opcion == "2":
        # Depositar dinero en una cuenta existente
        nombre = input("Cuenta a depositar: ")
        if nombre in cuentas:
            monto = float(input("Monto: "))
            cuentas[nombre].depositar(monto)  # Llama al método depositar
        else:
            print("Cuenta no encontrada.")

    elif opcion == "3":
        # Retirar dinero de una cuenta existente
        nombre = input("Cuenta a retirar: ")
        if nombre in cuentas:
            monto = float(input("Monto: "))
            if not cuentas[nombre].retirar(monto):
                print("Fondos insuficientes.")
        else:
            print("Cuenta no encontrada.")

    elif opcion == "4":
        # Mostrar todas las cuentas con su saldo
        for cuenta in cuentas.values():
            print(f"{cuenta.nombre} - Saldo: ${cuenta.saldo}")

    elif opcion == "0":
        # Salir del programa
        break

    else:
        print("Opción inválida.")
