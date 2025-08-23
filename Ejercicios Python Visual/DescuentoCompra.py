# 10 Descuento por compra
print("Este algoritmo nos ayudara a calcular un descuento en una compra que supere los 100$ ")

Compra = float(input("Ingresa el valor de tu compra: "))

if Compra > 100:
    Descuento = Compra * 0.10
    Total = Compra - Descuento
    print("Se aplica un 10% de descuento a tu compra. Total a pagar:", Total)
    
else:
    print("No se aplica descuento por tu compra. Total a pagar:", Compra)