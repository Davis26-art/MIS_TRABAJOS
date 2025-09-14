#--------------------------------------------------
# EJERCICIO FINAL 1 -- Calculadora científica
#--------------------------------------------------

# Mensaje inicial para el usuario.
print("Calculadora científica")

# Bucle principal: se repite hasta que el usuario escriba 'q' para salir.
while True:
    # Muestro las opciones disponibles para que el usuario elija.
    print("\nOperaciones:")
    print("1) Sumar     2) Restar    3) Multiplicar   4) Dividir")
    print("5) Potencia  6) Raíz      7) Factorial     q) Salir")

    # Tomo la opción elegida, elimino espacios al inicio/fin y la paso a minúsculas.
    # Esto permite que el usuario ponga 'Q', ' q ' o 'q' sin problemas.
    op = input("Elige una opción: ").strip().lower()

    # Si el usuario quiere salir, cierro el programa con un mensaje corto.
    if op == 'q':
        print("Chau. Usa con cabeza.")
        break

    # Uso try/except para atrapar conversiones inválidas (ej.: si el usuario escribe "dos").
    try:
        # Estas operaciones requieren dos números (a y b).
        if op in ('1','2','3','4','5'):
            # Convierto las entradas a float para aceptar decimales.
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))

            # Suma
            if op == '1':
                print(f"Resultado: {a + b}")

            # Resta
            elif op == '2':
                print(f"Resultado: {a - b}")

            # Multiplicación
            elif op == '3':
                print(f"Resultado: {a * b}")

            # División (con control de división por cero)
            elif op == '4':
                if b == 0:
                    # Evitamos la excepción y avisamos al usuario.
                    print("Error: división por cero.")
                else:
                    print(f"Resultado: {a / b}")

            # Potencia: a elevado a b (acepta exponentes fraccionarios y negativos).
            elif op == '5':
                print(f"Resultado: {a ** b}")

        # Raíz: pedimos el grado n y el número x (calculamos la raíz n-ésima de x).
        elif op == '6':
            # n puede ser decimal aquí, pero en la práctica suele ser entero (2, 3, ...).
            n = float(input("Grado de la raíz: "))
            x = float(input("Número: "))

            # Raíz de grado 0 no está definida — lo controlamos.
            if n == 0:
                print("Error: raíz de grado 0 no definida.")
            else:
                # Si x es negativo y la raíz es de grado par, no hay resultado real.
                # Aquí se usa int(n) para comprobar la paridad — es una simplificación:
                # si el usuario pone n no entero, la 'paridad' de int(n) puede no ser lo ideal.
                if x < 0 and int(n) % 2 == 0:
                    print("No se puede (raíz par de número negativo).")
                else:
                    # Calculamos la raíz como x ** (1/n). Esto funciona bien para n ≠ 0.
                    print(f"Resultado: {x ** (1/n)}")

        # Factorial: pedimos un entero no negativo y lo calculamos con un bucle.
        elif op == '7':
            # Leemos la entrada como texto para validar con isdigit().
            n = input("Número entero no negativo para factorial: ").strip()

            # isdigit() devuelve True solo si la cadena contiene solo dígitos (sin signo ni punto).
            # Eso evita negativos y decimales. Ej.: "5" -> True, "5.0" -> False, "-3" -> False.
            if not n.isdigit():
                print("Error: el factorial necesita un entero >= 0.")
            else:
                # Convertimos a int y calculamos el factorial de forma iterativa.
                n = int(n)
                resultado = 1
                # Multiplicamos 1*2*3*...*n
                for i in range(1, n + 1):
                    resultado *= i
                print(f"Resultado: {resultado}")

        # Si el usuario puso otra cosa, le aviso que la opción no es válida.
        else:
            print("Opción no válida. Elige 1-7 o q.")

    # Captura genérica si alguna conversión a float/ int falla.
    except ValueError:
        print("Entrada inválida: pon números válidos.")
