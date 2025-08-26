# Versión con WHILE

# Lista vacía para los segmentos
segmentos = []

i = 1
while i <= 7:
    valor = int(input(f"Digite un valor entre 1 y 0 para el segmento {i}: "))
    segmentos.append(valor)
    i += 1

# Asignamos valores
Seg_a, Seg_b, Seg_c, Seg_d, Seg_e, Seg_f, Seg_g = segmentos

# Condicionales
if Seg_a == 0 and Seg_b == 1 and Seg_c == 1 and Seg_d == 0 and Seg_e == 0 and Seg_f == 0 and Seg_g == 0:
    print("Este valor es 1.")
elif Seg_a == 1 and Seg_b == 1 and Seg_c == 0 and Seg_d == 1 and Seg_e == 1 and Seg_f == 0 and Seg_g == 1:
    print("Este valor es 2.")
elif Seg_a == 1 and Seg_b == 1 and Seg_c == 1 and Seg_d == 1 and Seg_e == 0 and Seg_f == 0 and Seg_g == 1:
    print("Este valor es 3.")
elif Seg_a == 0 and Seg_b == 1 and Seg_c == 1 and Seg_d == 0 and Seg_e == 0 and Seg_f == 1 and Seg_g == 1:
    print("Este valor es 4.")
elif Seg_a == 1 and Seg_b == 0 and Seg_c == 1 and Seg_d == 1 and Seg_e == 0 and Seg_f == 1 and Seg_g == 1:
    print("Este valor es 5.")
elif Seg_a == 1 and Seg_b == 0 and Seg_c == 1 and Seg_d == 1 and Seg_e == 1 and Seg_f == 1 and Seg_g == 1:
    print("Este valor es 6.")
elif Seg_a == 1 and Seg_b == 1 and Seg_c == 1 and Seg_d == 0 and Seg_e == 0 and Seg_f == 0 and Seg_g == 0:
    print("Este valor es 7.")
elif Seg_a == 1 and Seg_b == 1 and Seg_c == 1 and Seg_d == 1 and Seg_e == 1 and Seg_f == 1 and Seg_g == 1:
    print("Este valor es 8.")
elif Seg_a == 1 and Seg_b == 1 and Seg_c == 1 and Seg_d == 1 and Seg_e == 0 and Seg_f == 1 and Seg_g == 1:
    print("Este valor es 9.")
elif Seg_a == 1 and Seg_b == 1 and Seg_c == 1 and Seg_d == 1 and Seg_e == 1 and Seg_f == 1 and Seg_g == 0:
    print("Este valor es 0.")
else:
    print("Este valor es un error.")
