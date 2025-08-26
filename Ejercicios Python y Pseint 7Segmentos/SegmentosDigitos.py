#Peticion de numeros:

Seg_a = int(input("Digite un valor entre 1 y 0: "))
Seg_b = int(input("Digite un valor entre 1 y 0: "))
Seg_c = int(input("Digite un valor entre 1 y 0: "))
Seg_d = int(input("Digite un valor entre 1 y 0: "))
Seg_e = int(input("Digite un valor entre 1 y 0: "))
Seg_f = int(input("Digite un valor entre 1 y 0: "))
Seg_g = int(input("Digite un valor entre 1 y 0: "))


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
    print("Este valor es un error. ")


