#--------------------------------------------------
# EJERCICIO FINAL 3 -- Analizador de datos CSV
#--------------------------------------------------

print("📊 Analizador de datos CSV")

# Pedimos el nombre del archivo CSV.
archivo = input("Nombre del archivo CSV (ej: datos.csv): ").strip()

try:
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()  # Lee todas las líneas en una lista
except FileNotFoundError:
    print("⚠ No se encontró el archivo, revisa el nombre.")
    exit()

# Quitamos saltos de línea y dividimos cada línea en columnas usando coma.
datos = []
for linea in lineas:
    partes = linea.strip().split(",")
    datos.append(partes)

# Mostramos cuántas filas y columnas hay.
print(f"\n📄 El archivo tiene {len(datos)} filas y {len(datos[0])} columnas.")

# Suponemos que la primera fila es encabezado.
encabezado = datos[0]
filas = datos[1:]  # resto de filas son datos

print("\nEncabezado:", encabezado)

# Calculamos estadísticas por columna numérica.
for col in range(len(encabezado)):
    # Extraemos los valores de esta columna.
    columna = []
    for fila in filas:
        if col < len(fila):
            valor = fila[col].strip()
            # Si el valor es numérico lo convertimos a float, si no lo ignoramos.
            if valor.replace(".", "", 1).isdigit():
                columna.append(float(valor))

    # Si encontramos números, sacamos estadísticas.
    if columna:
        cantidad = len(columna)
        suma = 0
        minimo = columna[0]
        maximo = columna[0]

        # Recorremos para calcular suma, min y max sin usar imports.
        for v in columna:
            suma += v
            if v < minimo:
                minimo = v
            if v > maximo:
                maximo = v

        promedio = suma / cantidad
        print(f"\n📈 Columna: {encabezado[col]}")
        print(f"- Cantidad de datos: {cantidad}")
        print(f"- Suma total: {suma}")
        print(f"- Promedio: {promedio}")
        print(f"- Mínimo: {minimo}")
        print(f"- Máximo: {maximo}")

        # Dibujamos un gráfico de barras de texto simple
        print("Gráfico de barras (cada * vale 1 unidad):")
        for v in columna:
            print(f"{v:>6}: " + "*" * int(v))  # convierte el número en tantas barras

    else:
        print(f"\nℹ Columna: {encabezado[col]} (no es numérica, se ignora en estadísticas)")
