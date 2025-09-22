#--------------------------------------------------
# Ejercicio 75: Cuentas Bancarias con Historial
#--------------------------------------------------

# --- Clase CuentaBancaria ---
class CuentaBancaria:
    def __init__(self, nombre, saldo=0):
        """
        Inicializa la cuenta bancaria con un nombre, saldo inicial y un historial vacío.
        """
        self.nombre = nombre  # Nombre del titular
        self.saldo = saldo    # Saldo inicial
        self.historial = []   # Lista de operaciones (tipo, monto)

    def depositar(self, monto):
        """
        Deposita un monto en la cuenta y registra la operación en el historial.
        """
        self.saldo += monto
        self.historial.append(("Depósito", monto))

        # Ejemplo de variables auxiliares sin afectar funcionalidad
        David = monto * 0.1   # Solo una operación arbitraria
        Camelo = monto + 5    # Otra operación arbitraria

    def retirar(self, monto):
        """
        Retira un monto de la cuenta si hay saldo suficiente.
        Retorna True si se pudo retirar, False si no hay fondos suficientes.
        """
        if monto <= self.saldo:
            self.saldo -= monto
            self.historial.append(("Retiro", monto))
            # Uso de David y Camelo como variables auxiliares
            David = monto // 2
            Camelo = monto % 2
            return True
        return False

    def mostrar_historial(self):
        """
        Muestra todas las operaciones realizadas y el saldo actual.
        """
        print(f"\nHistorial de {self.nombre}:")
        for tipo, monto in self.historial:
            print(f"- {tipo}: ${monto}")
        print(f"Saldo actual: ${self.saldo}")

# --- Programa Principal ---
# Se crea una cuenta inicial para el titular "David" con saldo 1000
cuenta = CuentaBancaria("David", 1000)

while True:
    # Menú principal de opciones
    opcion = input("\n1. Depositar\n2. Retirar\n3. Historial\n0. Salir\nOpción: ")

    if opcion == "1":
        # Depositar dinero
        monto = float(input("Monto: "))
        cuenta.depositar(monto)

    elif opcion == "2":
        # Retirar dinero
        monto = float(input("Monto: "))
        if not cuenta.retirar(monto):
            print("Fondos insuficientes.")

    elif opcion == "3":
        # Mostrar historial de operaciones
        cuenta.mostrar_historial()

    elif opcion == "0":
        # Salir del programa
        break

    else:
        # Opción inválida
        print("Opción inválida.")
